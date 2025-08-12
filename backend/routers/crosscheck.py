from fastapi import APIRouter, Request, HTTPException
from backend.services.ai_service import generate_doctor_questions
import logging
router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/crosscheck")
async def crosscheck(request: Request):
    try:
        data = await request.json()
        if not isinstance(data, dict):
            logging.error("Malformed request: not a JSON object")
            raise HTTPException(status_code=400, detail="Malformed request body.")
        lab_results = data.get("lab_results", [])
        medicines = data.get("medicines", [])
        if not isinstance(lab_results, list) or not isinstance(medicines, list):
            logging.error("Malformed request: lab_results or medicines not lists")
            raise HTTPException(status_code=400, detail="lab_results and medicines must be lists.")
        questions = generate_doctor_questions(lab_results, medicines)
        logging.info("Doctor questions generated.")
        return {"notes": questions}
    except Exception as e:
        logging.error(f"Error in crosscheck: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating doctor questions: {e}")
