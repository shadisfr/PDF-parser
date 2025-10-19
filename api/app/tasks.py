import os
import requests
from .celery_app import celery_app

TIKA_URL = os.getenv("TIKA_SERVER_URL", "http://tika:9998").rstrip("/") + "/tika"

@celery_app.task(bind=True, name="process_pdf_task")
def process_pdf_task(self, file_path: str) -> str:
    """
    Celery task:
    - Reads the uploaded PDF from a shared volume
    - Sends it to Tika Server to extract text
    - Deletes the file afterwards
    - Returns the extracted text (stored in Redis by Celery)
    """
    try:
        with open(file_path, "rb") as f:
            resp = requests.put(
                TIKA_URL,
                data=f,
                headers={"Accept": "text/plain"},
                timeout=180,
            )
        resp.raise_for_status()
        text = resp.text
        return text
    except Exception as e:
        raise e
    finally:
        # Clean up regardless of success or failure
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception:
            # Avoid masking the original error
            pass
