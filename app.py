from cs50 import SQL
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///todos.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # get all the important index
    db_index = db.execute("SELECT id, status, todo, GROUP_CONCAT(name, ', ') AS tags, date, time FROM todos LEFT OUTER JOIN (SELECT todo_id, name FROM tagging JOIN tags ON tagging.tag_id == tags.id) AS tags ON todos.id = tags.todo_id WHERE user_id = ? GROUP BY id ORDER BY status DESC, date, time", session["user_id"])
    return render_template("index.html", todos=db_index)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must provide confirmation password", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password and confirmation don't match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username not already exists
        for i in range(len(rows)):
            if request.form.get("username") == rows[i]["username"]:
                return apology("username already exists", 400)

        passcode = generate_password_hash(request.form.get("password"))

        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get("username"), passcode)

        return redirect("/login")
    return render_template("register.html")


@app.route("/TODO", methods=["POST"])
def TODO():
    # get the todo_id
    todo_id = request.form.get("todo_id")
    # change status to DONE
    db.execute("UPDATE todos SET status = 'DONE' WHERE user_id = ? AND id = ?", session["user_id"], todo_id)
    return redirect("/")


@app.route("/DONE", methods=["POST"])
def DONE():
    # get the todo_id
    todo_id = request.form.get("todo_id")
    # change status to TODO
    db.execute("UPDATE todos SET status = 'TODO' WHERE user_id = ? AND id = ?", session["user_id"], todo_id)
    return redirect("/")


@app.route("/DELETE", methods=["POST"])
def DELETE():
    # get the todo_id
    todo_id = request.form.get("todo_id")
    # delete from tagging and todos
    db.execute("DELETE FROM tagging WHERE user_id = ? AND todo_id = ?", session["user_id"], todo_id)
    db.execute("DELETE FROM todos WHERE user_id = ? AND id = ?", session["user_id"], todo_id)
    return redirect("/")


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html", tags=db.execute("SELECT * FROM tags WHERE user_id = ?", session["user_id"]))
    
    todo = request.form.get("todo")
    tags = request.form.getlist("tags")
    date = request.form.get("date")
    time = request.form.get("time")

    db.execute("INSERT INTO todos (user_id, todo, date, time) VALUES (?, ?, ?, ?)", session["user_id"], todo, date, time)
    
    if len(tags) > 0:
        # get the last added item from todo.db
        todo_id = db.execute("SELECT id FROM todos WHERE user_id = ? ORDER BY id DESC LIMIT 1", session["user_id"])[0]["id"]
        for tag in tags:
            db.execute("INSERT INTO tagging (user_id, tag_id, todo_id) VALUES (?, ?, ?)", session["user_id"], tag, todo_id)

    return redirect("/")


@app.route("/tags", methods=["GET", "POST"])
def tags():
    if request.method == "GET":
        return render_template("tags.html", tags=db.execute("SELECT * FROM tags WHERE user_id = ?", session["user_id"]))

    db.execute("INSERT INTO tags (user_id, name) VALUES (?, ?)", session["user_id"], request.form.get("name"))

    return redirect("/tags")


@app.route("/tag_edit", methods=["POST"])
def tag_edit():
    # get the new_name and tag id
    new_name = request.form.get("new_name")
    tag_id = request.form.get("tag_id")
    # update tags table
    db.execute("UPDATE tags SET name = ? WHERE id = ? AND user_id = ?", new_name, tag_id, session["user_id"])
    return redirect('/tags')


@app.route("/tag_delete", methods=["POST"])
def tag_delete():
    # get the tag_id
    tag_id = request.form.get("tag_id")
    # delete from tagging and tags
    db.execute("DELETE FROM tagging WHERE tag_id = ? AND user_id = ?", tag_id, session["user_id"])
    db.execute("DELETE FROM tags WHERE id = ? AND user_id = ?", tag_id, session["user_id"])
    return redirect("/tags")
    