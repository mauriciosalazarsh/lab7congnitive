from flask import Flask, jsonify
import mysql.connector
from rds_config import rds_host, db_user, db_password, db_name

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host=rds_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

@app.route("/catalogo")
def catalogo():
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT id, marca, modelo, precio FROM vehiculos")
    rows = cur.fetchall()
    con.close()

    data = [
        {"id": r[0], "marca": r[1], "modelo": r[2], "precio": float(r[3])}
        for r in rows
    ]
    return jsonify(data)
