# Cross-check service stub
def crosscheck_lab_and_prescription(lab_results, medicines):
    issues = []
    # Example rule: High glucose but no diabetes medication
    high_glucose = any(r.get("param") == "Glucose" and r.get("status") == "high" for r in lab_results)
    diabetes_meds = any(m.get("name").lower() in ["metformin", "insulin"] for m in medicines)
    if high_glucose and not diabetes_meds:
        issues.append({
            "issue": "High glucose",
            "note": "No diabetes medication prescribed; ask doctor if follow-up HbA1c test needed"
        })
    # Example rule: Antibiotic prescribed but no infection marker
    antibiotics = [m for m in medicines if m.get("name").lower() in ["amoxicillin", "azithromycin"]]
    infection_marker = any(r.get("param") == "WBC" and r.get("status") == "high" for r in lab_results)
    if antibiotics and not infection_marker:
        issues.append({
            "issue": "Antibiotic prescribed",
            "note": "Is this antibiotic necessary without infection markers?"
        })
    return issues
