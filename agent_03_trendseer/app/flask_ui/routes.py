from flask import render_template, redirect, url_for
import sqlite3
import subprocess
from datetime import datetime

def register_routes(app):
    # 🧠 DASHBOARD VIEW
    @app.route("/dashboard")
    def dashboard():
        conn = sqlite3.connect("data/summaries.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("""
            SELECT domain, title, summary, tags, date
            FROM summaries
            ORDER BY date DESC
            LIMIT 25
        """)
        rows = cursor.fetchall()
        conn.close()

        # Group by domain
        grouped = {}
        for row in rows:
            domain = row["domain"]
            grouped.setdefault(domain, []).append(row)

        return render_template("dashboard.html", grouped=grouped, timestamp=datetime.utcnow())

    # 🚀 TRIGGER AGENT_03 MANUALLY
    @app.route("/run-agent", methods=["POST"])
    def run_agent():
        try:
            print("⚙️  Running agent_03.py...")
            subprocess.run(["python3", "agent_03.py"], check=True)
            print("✅ agent_03.py completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running agent_03.py: {e}")
        return redirect(url_for("dashboard"))
