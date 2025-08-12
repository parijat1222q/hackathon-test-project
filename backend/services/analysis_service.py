import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from backend.models.health_ranges import HEALTH_RANGES

def analyze_lab_results(lab_results):
    # Convert to DataFrame for analysis
    df = pd.DataFrame(lab_results)
    analyzed = []
    # Basic abnormal value detection
    for _, result in df.iterrows():
        param = result.get("param")
        value = result.get("value")
        unit = result.get("unit")
        ref_range = HEALTH_RANGES.get(param, (None, None))
        status = "normal"
        color = "green"
        if ref_range[0] is not None and value < ref_range[0]:
            status = "low"
            color = "blue"
        elif ref_range[1] is not None and value > ref_range[1]:
            status = "high"
            color = "red"
        analyzed.append({
            "param": param,
            "value": value,
            "unit": unit,
            "ref_range": f"{ref_range[0]}-{ref_range[1]}",
            "status": status,
            "color": color
        })
    # Advanced: Outlier detection (Isolation Forest)
    if not df.empty and "value" in df:
        values = df["value"].values.reshape(-1, 1)
        clf = IsolationForest(contamination=0.1)
        outliers = clf.fit_predict(values)
        for i, outlier in enumerate(outliers):
            if outlier == -1:
                analyzed[i]["outlier"] = True
            else:
                analyzed[i]["outlier"] = False
    # Statistical summary
    stats = {}
    if not df.empty and "value" in df:
        stats = {
            "mean": float(np.mean(df["value"])),
            "std": float(np.std(df["value"])),
            "min": float(np.min(df["value"])),
            "max": float(np.max(df["value"])),
        }
    return {"analyzed": analyzed, "stats": stats}
