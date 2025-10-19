import os
import uuid
from fastapi import UploadFile
import aiofiles

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/data/uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_upload_file(file: UploadFile) -> str:
    # Always store as .pdf (we already validate extension in the endpoint)
    filename = f"{uuid.uuid4().hex}.pdf"
    dest_path = os.path.join(UPLOAD_DIR, filename)

    # Stream to disk to avoid memory spikes
    async with aiofiles.open(dest_path, "wb") as out:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            await out.write(chunk)

    await file.close()
    return dest_path
