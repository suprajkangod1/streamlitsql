
import json
import re

# Example rules (could be loaded from a JSON/YAML config in practice)
DEFAULT_RULES = [
    {"type": "block", "pattern": "DROP\s+TABLE", "message": "Drop table is not allowed."},
    {"type": "block", "pattern": "JOIN.*sensitive_data", "message": "Joining with sensitive data is restricted."},
    {"type": "warn", "pattern": "SELECT\s+\*", "message": "Selecting all columns may be inefficient."}
]

def check_query_rules(sql: str, rules: list = None) -> dict:
    """
    Check a SQL query against a set of rules and return violations.
    Rules can block or warn based on regex patterns.
    """
    rules = rules or DEFAULT_RULES
    blocks = []
    warnings = []

    for rule in rules:
        if re.search(rule["pattern"], sql, re.IGNORECASE):
            if rule["type"] == "block":
                blocks.append(rule["message"])
            elif rule["type"] == "warn":
                warnings.append(rule["message"])

    return {
        "blocked": bool(blocks),
        "blocks": blocks,
        "warnings": warnings
    }
