import os
import sqlite3
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = os.urandom(24)

# API kulcs beállítása
API_KEY = os.environ.get("GOOGLE_API_KEY")

# Adatbázis létrehozása
def init_db():
    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS results (
                      domain TEXT,
                      result TEXT,
                      date TEXT)
                   """)
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        domain = request.form["domain"]
        response = requests.get(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}", json={
            "client": {
                "clientId": "flask_app",
                "clientVersion": "1.0.0"
            },
            "threatInfo": {
                "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
                "platformTypes": ["ANY_PLATFORM"],
                "threatEntryTypes": ["URL"],
                "threatEntries": [{"url": domain}]
            }
        })

        is_infected = len(response.json().get("matches", [])) > 0
        result = "Fertőzött" if is_infected else "Nem fertőzött"
        color = "danger" if is_infected else "success"

        # Eredmény mentése az adatbázisba
        conn = sqlite3.connect("results.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO results (domain, result, date) VALUES (?, ?, ?)", (domain, result, datetime.now()))
        conn.commit()
        conn.close()

        flash(result, color)
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
