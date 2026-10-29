# Data Quality Sentinel

Automated rule-based and statistical data integrity auditor. Inspects datasets for schema drift, temporal sequence violations, status lifecycle anomalies, and duplicate identifiers.

## Key Capabilities
- **Schema & Type Guard**: Validates incoming datasets against declarative typing contracts.
- **Temporal Order Invariance**: Catches impossible timestamps (e.g., `resolution_time < creation_time`).
- **Uniqueness & Referential Checks**: Validates primary keys and foreign key constraints across partitioned batch snapshots.

## Usage
```bash
pip install -r requirements.txt
python main.py
pytest tests/
```
