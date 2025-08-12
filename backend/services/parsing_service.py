# Parsing service stub
import re
from backend.models.health_ranges import HEALTH_RANGES
from backend.utils.regex_patterns import LAB_PARAM_PATTERN, MEDICINE_PATTERN

def parse_lab_parameters(text: str):
    results = []
    # Example regex: param value unit
    pattern = re.compile(rf"({LAB_PARAM_PATTERN})\s*[:\-]?\s*(\d+(\.\d+)?)\s*([a-zA-Z/\^]+)")
    for match in pattern.finditer(text):
        param = match.group(1)
        value = float(match.group(2))
        unit = match.group(4)
        ref_range = HEALTH_RANGES.get(param, (None, None))
        status = "normal"
        if ref_range[0] is not None and value < ref_range[0]:
            status = "low"
        elif ref_range[1] is not None and value > ref_range[1]:
            status = "high"
        results.append({
            "param": param,
            "value": value,
            "unit": unit,
            "ref_range": f"{ref_range[0]}-{ref_range[1]}",
            "status": status
        })
    return results

def parse_medicines(text: str):
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
