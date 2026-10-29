import pandas as pd
from src.auditor import DataQualityAuditor

def main():
    print("=== Data Quality Sentinel Audit ===")
    sample_data = pd.DataFrame([
        {"id": "EVT-1", "created_at": "2026-01-01 10:00:00", "resolved_at": "2026-01-01 10:30:00", "status": "OK"},
        {"id": "EVT-2", "created_at": "2026-01-01 11:00:00", "resolved_at": "2026-01-01 10:00:00", "status": "ERROR"},
        {"id": "EVT-3", "created_at": "2026-01-01 12:00:00", "resolved_at": "2026-01-01 12:15:00", "status": None},
        {"id": "EVT-1", "created_at": "2026-01-01 13:00:00", "resolved_at": "2026-01-01 13:45:00", "status": "OK"}
    ])
    
    auditor = DataQualityAuditor(primary_key="id")
    result = auditor.audit_dataframe(sample_data)
    
    print("Scanned: " + str(result['total_records_scanned']) + " records")
    print("Integrity Status: " + ("PASSED" if result['passed'] else "FAILED"))
    print("Findings:")
    for f in result["findings"]:
        print(" - " + f)

if __name__ == '__main__':
    main()
