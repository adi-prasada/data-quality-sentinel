import pandas as pd
from typing import Dict, List, Any

class DataQualityAuditor:
    def __init__(self, primary_key: str):
        self.primary_key = primary_key
        
    def audit_dataframe(self, df: pd.DataFrame) -> Dict[str, Any]:
        total_rows = len(df)
        findings = []
        
        null_pks = df[self.primary_key].isnull().sum()
        if null_pks > 0:
            findings.append("CRITICAL: Found null values in primary key " + str(self.primary_key))
            
        dup_pks = df[self.primary_key].duplicated().sum()
        if dup_pks > 0:
            findings.append("CRITICAL: Found " + str(dup_pks) + " duplicate primary keys")
            
        if "created_at" in df.columns and "resolved_at" in df.columns:
            temporal_errors = (pd.to_datetime(df["resolved_at"], errors="coerce") < pd.to_datetime(df["created_at"], errors="coerce")).sum()
            if temporal_errors > 0:
                findings.append("WARNING: Found " + str(temporal_errors) + " records where resolved_at is prior to created_at")
                
        if "status" in df.columns:
            invalid_status = df["status"].isnull().sum()
            if invalid_status > 0:
                findings.append("WARNING: Found " + str(invalid_status) + " records with null status")
                
        status_pass = len([f for f in findings if f.startswith("CRITICAL")]) == 0
        return {
            "total_records_scanned": total_rows,
            "passed": status_pass,
            "anomaly_count": len(findings),
            "findings": findings
        }
