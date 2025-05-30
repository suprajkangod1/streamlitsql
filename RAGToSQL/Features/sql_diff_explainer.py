
import difflib

def explain_sql_diff(user_sql: str, ai_sql: str) -> str:
    """
    Generate a line-by-line explanation of the differences between user and AI SQL.
    """
    user_lines = user_sql.strip().splitlines()
    ai_lines = ai_sql.strip().splitlines()

    diff = difflib.unified_diff(user_lines, ai_lines, fromfile="user_sql", tofile="ai_sql", lineterm="")

    explanation = "\n".join(diff)
    return explanation or "No differences found. SQL statements are identical."
