
import sqlparse

def explain_query(sql: str, schema_tables: list) -> dict:
    """
    Return a breakdown of the SQL query including:
    - parsed structure
    - referenced tables/columns
    - a transparency score (mocked for now)
    """
    try:
        # Parse SQL using sqlparse
        parsed = sqlparse.parse(sql)[0]
        tokens = [t.value for t in parsed.tokens if not t.is_whitespace]

        # Very basic table/column extraction (could use sql_metadata or custom logic)
        referenced = [token for token in tokens if any(tbl in token for tbl in schema_tables)]

        score = 100 if len(referenced) else 40  # Simple trust score logic

        return {
            "tokens": tokens,
            "referenced_tables": referenced,
            "transparency_score": score
        }
    except Exception as e:
        return {"error": str(e)}
