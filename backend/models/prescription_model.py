# Prescription data model stub
from pydantic import BaseModel

class Medicine(BaseModel):
    name: str
    dose: str
    freq: str
    duration: str

class Prescription(BaseModel):
    medicines: list[Medicine]
