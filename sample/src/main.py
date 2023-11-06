import os
import psycopg2

from flask import Flask


POSTGRES_CONNECTION_STRING = os.getenv("POSTGRES_CONNECTION_STRING")

app = Flask(__name__)


@app.get("/")
def index():
    return "Hello; from sample"


@app.get("/sql_test")
def sql_test():
    conn = psycopg2.connect(POSTGRES_CONNECTION_STRING)
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()[0]
    cur.close()
    conn.close()

    return f"The database returned {result}"


if __name__ == "__main__":
    app.run(host="localhost", port=80, debug=True)
