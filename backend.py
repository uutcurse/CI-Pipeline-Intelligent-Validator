from fastapi import FastAPI, UploadFile, File
import tempfile
import os

from notebooks.brain_core import CIPipelineValidator

app = FastAPI(title="CI Risk Validator API")

validator = CIPipelineValidator()


@app.post("/analyze")
async def analyze_pipeline(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        result = validator.validate_file_dict(tmp_path)
        return result
    finally:
        os.remove(tmp_path)
