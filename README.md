# MedScan – AI Symptom & Report Analyzer

## Project Overview
MedScan is a full-stack hackathon project designed to automate and enhance the analysis of medical reports and prescriptions using AI, OCR, and advanced data science techniques. The backend is built with FastAPI and Python, while the frontend (to be integrated) will provide a user-friendly interface for uploading, analyzing, and summarizing medical documents.

## Features
- **Upload & OCR**: Accepts PDF and image uploads of lab reports and prescriptions, extracts text using Tesseract OCR.
- **Regex Parsing**: Extracts lab parameters and medicines using robust regex patterns.
- **AI Summarization & NER**: Uses HuggingFace models for summarizing medical text and extracting keywords/entities.
- **Advanced Analysis**: Applies Pandas, NumPy, and scikit-learn for lab value analysis, outlier detection, and health insights.
- **PDF Generation**: Generates styled PDF reports using Jinja2 and WeasyPrint.
- **Crosscheck & Research**: Crosschecks lab results with prescriptions and fetches PubMed research links.
- **Validation & Security**: Validates file types/sizes, handles errors robustly, and cleans up uploads.
- **Automated Testing**: Comprehensive unit/integration tests for all endpoints and services.

## Backend Structure
- `backend/main.py`: FastAPI app, router setup, CORS.
- `backend/routers/`: API endpoints for upload, analysis, crosscheck, research, report, summarize.
- `backend/services/`: OCR, parsing, analysis, AI, PDF generation logic.
- `backend/utils/`: Regex patterns, file utilities, units normalization.
- `backend/models/`: Data models and healthy ranges.
- `backend/templates/`: Jinja2 HTML templates for PDF reports.
- `backend/tests/`: Automated tests for endpoints and services.

## Setup Instructions
1. **Clone the repo** and navigate to the `meta` folder.
2. **Create and activate a Python virtual environment**:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r backend/requirements.txt
   pip install torch
   ```
4. **Configure environment variables**:
   - Copy `backend/.env.example` to `backend/.env` and fill in required values (e.g., `PUBMED_API_KEY`).
5. **Install Tesseract OCR** (Linux):
   ```sh
   sudo apt-get install tesseract-ocr
   ```
6. **Run the backend server**:
   ```sh
   uvicorn backend.main:app --reload
   ```
7. **Access API docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

## Project Discussion
MedScan aims to streamline medical data analysis for patients and healthcare professionals. By combining OCR, regex, and AI, it automates extraction and interpretation of lab results and prescriptions. The backend is modular, robust, and production-ready, with strong validation, error handling, and test coverage. Future work includes frontend integration, user authentication, and more advanced analytics.

## Hackathon Value
- Rapid, automated medical report analysis
- AI-powered insights and summaries
- Secure, reliable backend with full test coverage
- Ready for integration with modern frontend frameworks

---
For questions or contributions, contact the project owner or open an issue in the repository.
