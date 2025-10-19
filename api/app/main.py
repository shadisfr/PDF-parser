from fastapi import FastAPI, UploadFile, File, HTTPException
from .models import TaskResponse, TaskStatusResponse
from .utils import save_upload_file
from .tasks import process_pdf_task
from .celery_app import celery_app

app = FastAPI(title="Doc Processing API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/upload/", response_model=TaskResponse)
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")

    file_path = await save_upload_file(file)
    task = process_pdf_task.delay(file_path)
    return {"task_id": task.id}

@app.get("/task/{task_id}", response_model=TaskStatusResponse)
def get_task_status(task_id: str):
    res = celery_app.AsyncResult(task_id)

    if res.failed():
        return {"status": "failed", "result": str(res.result)}

    if not res.ready():
        return {"status": "processing", "result": None}

    # Completed
    return {"status": "completed", "result": res.result}
