# Report data model stub
from pydantic import BaseModel

class LabParameter(BaseModel):
    param: str
    value: float
    unit: str
    ref_range: str
    status: str

class LabReport(BaseModel):
    parameters: list[LabParameter]
