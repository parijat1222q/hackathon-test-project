import re
from backend.utils.regex_patterns import MEDICINE_PATTERN

# Prescription parsing service stub
def parse_prescription(text: str):
    medicines = []
    # Example regex: medicine dose freq duration
    pattern = re.compile(rf"({MEDICINE_PATTERN})\s*(\d+\s*mg)\s*(TID|BID|OD)\s*(\d+\s*days)")
    for match in pattern.finditer(text):
        name = match.group(1)
        dose = match.group(2)
        freq = match.group(3)
        duration = match.group(4)
        medicines.append({
            "name": name,
            "dose": dose,
            "freq": freq,
            "duration": duration
        })
    return medicines
