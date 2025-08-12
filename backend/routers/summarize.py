from fastapi import APIRouter, Request, HTTPException
from backend.services.ai_service import summarize_text, extract_medical_keywords
import logging
router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/summarize")
async def summarize(request: Request):
    try:
        data = await request.json()
        if not isinstance(data, dict):
            logging.error("Malformed request: not a JSON object")
            raise HTTPException(status_code=400, detail="Malformed request body.")
        text = data.get("text", "")
        if not text or not isinstance(text, str) or len(text.strip()) < 2:
            logging.error("Invalid text for summarization endpoint")
            raise HTTPException(status_code=400, detail="Text must be a non-empty string.")
        summary = summarize_text(text)
        keywords = extract_medical_keywords(text)
        logging.info("Text summarized and keywords extracted.")
        return {"summary": summary, "keywords": keywords}
    except Exception as e:
        logging.error(f"Error in summarize: {e}")
        raise HTTPException(status_code=500, detail=f"Error summarizing/extracting keywords: {e}")
