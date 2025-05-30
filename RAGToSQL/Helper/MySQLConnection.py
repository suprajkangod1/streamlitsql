
from sqlalchemy.engine import URL

def get_sqlalchemy_uri():
    # Edit these credentials as per your MySQL setup
    username = "root"
    password = "Welcome@123"
    host = "192.168.1.102"
    port = 3306
    database = "test"

    return URL.create(
        "mysql+pymysql",
        username=username,
        password=password,
        host=host,
        port=port,
        database=database
    )
    