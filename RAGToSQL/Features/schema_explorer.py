
import sqlalchemy

def fetch_schema_overview(engine):
    """
    Returns a dictionary of table names and their columns from a SQLAlchemy engine.
    """
    try:
        inspector = sqlalchemy.inspect(engine)
        schema = {}
        for table_name in inspector.get_table_names():
            columns = inspector.get_columns(table_name)
            schema[table_name] = [col["name"] for col in columns]
        return schema
    except Exception as e:
        return {"error": str(e)}
