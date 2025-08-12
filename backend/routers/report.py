from fastapi import APIRouter, Response, HTTPException
from backend.services.pdf_service import generate_pdf_report
import logging
router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.get("/report/{id}")
async def get_pdf_report(id: str):
    try:
        if not id or not isinstance(id, str) or len(id.strip()) < 2:
            logging.error("Invalid report id")
            raise HTTPException(status_code=400, detail="Report id must be a non-empty string.")
        pdf_data = generate_pdf_report({"id": id})
        logging.info(f"PDF report generated for id: {id}")
        return Response(content=pdf_data, media_type="application/pdf")
    except Exception as e:
        logging.error(f"Error in get_pdf_report: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF report: {e}")
