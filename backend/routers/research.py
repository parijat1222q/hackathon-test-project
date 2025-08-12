from fastapi import APIRouter, HTTPException
from backend.services.pubmed_service import search_pubmed
import logging
router = APIRouter()
logging.basicConfig(level=logging.INFO)

@router.get("/research")
async def get_research(term: str):
    try:
        if not term or not isinstance(term, str) or len(term.strip()) < 2:
            logging.error("Invalid search term for research endpoint")
            raise HTTPException(status_code=400, detail="Search term must be a non-empty string.")
        links = search_pubmed(term)
        logging.info(f"PubMed search completed for term: {term}")
        return {"links": links}
    except Exception as e:
        logging.error(f"Error in get_research: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching PubMed research: {e}")
