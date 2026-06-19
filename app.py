from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import sqlite3
from chatbot import get_bot_response

app = Flask(__name__)
app.secret_key = "mediassist_secret"

DATABASE = "database/healthcare.db"


def create_tables():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS reminders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medicine TEXT,
        reminder_time TEXT
    )
    """)

    conn.commit()
    conn.close()


create_tables()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/register_user", methods=["POST"])
def register_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )
        conn.commit()

    except:
        pass

    conn.close()

    return redirect(url_for("login"))


@app.route("/login_user", methods=["POST"])
def login_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cur.fetchone()

    conn.close()

    if user:
        session["user"] = username
        return redirect(url_for("dashboard"))

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    bot_response = get_bot_response(user_message)

    return jsonify({
        "response": bot_response
    })


@app.route("/add_reminder", methods=["POST"])
def add_reminder():

    medicine = request.form["medicine"]
    reminder_time = request.form["time"]

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO reminders(medicine,reminder_time) VALUES(?,?)",
        (medicine, reminder_time)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
