from fastapi import APIRouter, Request, HTTPException
from backend.services.crosscheck_service import crosscheck_lab_and_prescription
from backend.services.analysis_service import analyze_lab_results
import logging
router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.post("/analyze/crosscheck")
async def analyze_crosscheck(request: Request):
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
        analyzed = analyze_lab_results(lab_results)
        crosscheck = crosscheck_lab_and_prescription(lab_results, medicines)
        logging.info("Analysis and crosscheck completed.")
        return {"analyzed": analyzed, "crosscheck": crosscheck}
    except Exception as e:
        logging.error(f"Error in analyze_crosscheck: {e}")
        raise HTTPException(status_code=500, detail=f"Error analyzing/crosschecking: {e}")
