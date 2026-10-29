import pandas as pd
from src.auditor import DataQualityAuditor

def test_clean_data():
    df = pd.DataFrame([
        {"id": "1", "created_at": "2026-01-01 10:00:00", "resolved_at": "2026-01-01 11:00:00", "status": "DONE"}
    ])
    aud = DataQualityAuditor("id")
    res = aud.audit_dataframe(df)
    assert res["passed"] is True
    assert res["anomaly_count"] == 0
