import os
import shutil
import tempfile
from fastapi import UploadFile

async def save_upload_file_temporarily(upload_file: UploadFile) -> str:
    try:
        temp_dir = tempfile.mkdtemp()
        file_path = os.path.join(temp_dir, upload_file.filename)
        with open(file_path, "wb") as f:
            contents = await upload_file.read()
            f.write(contents)
        return file_path
    except Exception as e:
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        raise e