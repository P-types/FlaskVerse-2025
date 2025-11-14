from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

USERNAME = "admin"
PASSWORD = "admin123"

def logged():
    return "logged" in session

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == USERNAME and request.form["password"] == PASSWORD:
            session["logged"] = True
            return redirect("/")
        return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/")
def home():
    if not logged():
        return redirect("/login")
    return render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if not logged():
        return redirect("/login")
    if request.method == "POST":
        r = request.form["roll"]
        n = request.form["name"]
        m = request.form["marks"]
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("INSERT INTO students VALUES (?, ?, ?)", (r, n, m))
        con.commit()
        con.close()
        return redirect("/list")
    return render_template("add.html")

@app.route("/list")
def list_students():
    if not logged():
        return redirect("/login")
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    con.close()
    return render_template("list.html", data=data)

@app.route("/delete/<roll>")
def delete(roll):
    if not logged():
        return redirect("/login")
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    cur.execute("DELETE FROM students WHERE roll=?", (roll,))
    con.commit()
    con.close()
    return redirect("/list")

@app.route("/edit/<roll>", methods=["GET", "POST"])
def edit(roll):
    if not logged():
        return redirect("/login")
    con = sqlite3.connect("students.db")
    cur = con.cursor()
    if request.method == "POST":
        n = request.form["name"]
        m = request.form["marks"]
        cur.execute("UPDATE students SET name=?, marks=? WHERE roll=?", (n, m, roll))
        con.commit()
        con.close()
        return redirect("/list")
    cur.execute("SELECT * FROM students WHERE roll=?", (roll,))
    student = cur.fetchone()
    con.close()
    return render_template("edit.html", student=student)

@app.route("/filter", methods=["GET", "POST"])
def filter_students():
    if not logged():
        return redirect("/login")
    data = []
    if request.method == "POST":
        mn = request.form["min"]
        mx = request.form["max"]
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM students WHERE marks BETWEEN ? AND ?", (mn, mx))
        data = cur.fetchall()
        con.close()
    return render_template("filter.html", data=data)

@app.route("/search", methods=["GET", "POST"])
def search():
    if not logged():
        return redirect("/login")
    data = []
    if request.method == "POST":
        q = "%" + request.form["query"] + "%"
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM students WHERE roll LIKE ? OR name LIKE ?", (q, q))
        data = cur.fetchall()
        con.close()
    return render_template("search.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
