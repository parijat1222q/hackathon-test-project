from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.ocr_service import extract_text_from_image, extract_text_from_pdf
from backend.services.prescription_service import parse_prescription
from backend.utils.file_utils import save_upload
import os
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/upload/prescription")
async def upload_prescription(file: UploadFile = File(...)):
    try:
        # Validate file type
        if not (file.filename.lower().endswith(".pdf") or file.filename.lower().endswith((".png", ".jpg", ".jpeg"))):
            logging.error(f"Invalid file type: {file.filename}")
            raise HTTPException(status_code=400, detail="Only PDF and image files are allowed.")
        # Validate file size (max 5MB)
        contents = await file.read()
        if len(contents) > 5 * 1024 * 1024:
            logging.error(f"File too large: {file.filename}")
            raise HTTPException(status_code=413, detail="File size exceeds 5MB limit.")
        # Save uploaded file
        upload_dir = "static/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        if not save_upload(contents, file_path):
            logging.error(f"Failed to save file: {file.filename}")
            raise HTTPException(status_code=500, detail="Failed to save file.")
        logging.info(f"File saved: {file_path}")
        # Periodic cleanup of old uploads
        from backend.utils.file_utils import cleanup_uploads
        cleanup_uploads(upload_dir)
        # OCR extraction
        if file.filename.lower().endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            text = extract_text_from_image(file_path)
        logging.info(f"OCR text extracted for {file.filename}")
        # Parse medicines
        medicines = parse_prescription(text)
        logging.info(f"Medicines parsed for {file.filename}")
        return {"message": "Prescription uploaded", "medicines": medicines}
    except Exception as e:
        logging.error(f"Error in upload_prescription: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing prescription: {e}")
