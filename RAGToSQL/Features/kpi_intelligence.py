
def map_kpi_to_sql(kpi_text: str) -> str:
    """
    Map simple KPI prompts to SQL templates.
    Extend this with NLP parsing or prompt engineering for advanced use.
    """
    kpi_text = kpi_text.lower()

    if "total claims" in kpi_text and "state" in kpi_text:
        return "SELECT state, SUM(claim_amount) AS total_claims FROM claims GROUP BY state;"

    if "average claim" in kpi_text and "month" in kpi_text:
        return "SELECT MONTH(claim_date) AS month, AVG(claim_amount) AS avg_claim FROM claims GROUP BY MONTH(claim_date);"

    if "claim count by agent" in kpi_text:
        return "SELECT agent_id, COUNT(*) AS claim_count FROM claims GROUP BY agent_id;"

    return "-- Could not auto-map KPI to SQL. Please refine your prompt."
