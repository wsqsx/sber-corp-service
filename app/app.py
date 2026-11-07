import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/api/employees")
def employees():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    cur = conn.cursor()
    cur.execute("SELECT id, full_name, department FROM employees;")
    rows = [{"id": r[0], "full_name": r[1], "department": r[2]} for r in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)