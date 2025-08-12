# MedScan Backend

## Setup
1. Create a virtual environment and activate it.
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in values.
4. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

## Folder Structure
- routers/: API route definitions
- services/: Core business logic
- models/: Data models & schemas
- utils/: Helper functions
- static/uploads/: Uploaded files & generated PDFs
- tests/: Unit tests
