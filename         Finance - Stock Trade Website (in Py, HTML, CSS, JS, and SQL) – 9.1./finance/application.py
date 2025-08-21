import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # the user's curent cash
    usercash = db.execute("SELECT cash FROM users WHERE id = :Id", Id=session["user_id"])

    A = db.execute("SELECT symbole, name, ownedsharesnumber, currentprice, totalval FROM possession WHERE user_id = :Id AND ownedsharesnumber != 0", Id=session["user_id"])

    for row in A:
        dico = lookup(row["symbole"])
        row["currentprice"] = dico["price"]
        row["totalval"] = dico["price"] * row["ownedsharesnumber"]


    ST = db.execute("SELECT SUM(totalval) FROM possession WHERE user_id = :Id", Id=session["user_id"])

    if  ST[0]["SUM(totalval)"] == None:
        GT = usd(usercash[0]["cash"])

    else:
        GT = usd(usercash[0]["cash"] + ST[0]["SUM(totalval)"])

    for row in A:
        row["currentprice"] = usd(row["currentprice"])
        row["totalval"] = usd(row["totalval"])


    return render_template("index.html", cash=usd( usercash[0]["cash"] ), A = A, grandtotal=GT)





@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        dico = dict()
        symb = request.form.get("symbol")
        shar = int(request.form.get("shares"))
        dico = lookup(symb)


        if dico == None or not symb:
            return apology("MISSING SYMBOL", 400)

        if not shar:
            return apology("MISSING SHARES", 400)
        if shar < 1:
            return apology("VALUE MUST BE GREATER THAN OR EQUAL TO 1", 400)



        usercash = db.execute("SELECT cash FROM users WHERE id = :Id", Id=session["user_id"])

        total = dico["price"] * shar
        if total > usercash[0]["cash"]:
            return apology("CAN'T AFFORD", 400)


        db.execute("INSERT INTO history (user_id, symbole, name, price, sharesnumber, total, orderdate, ordertime) VALUES(:Id, :symb, :name, :price, :shar, :total, :date, :time)", Id=session["user_id"], symb=symb, name=dico["name"], price=dico["price"], shar=shar, total=total, date=datetime.now().date(), time=datetime.now().time())

        db.execute("UPDATE users SET cash = :cash WHERE id = :Id", cash=(usercash[0]["cash"]-total), Id=session["user_id"])

        # number of share of this business(symbole) the user already possessed
        OS = db.execute("SELECT ownedsharesnumber FROM possession WHERE user_id = :Id AND symbole = :symb", Id=session["user_id"], symb=symb)

        x = db.execute("SELECT * FROM possession WHERE user_id = :Id AND symbole = :symb", Id=session["user_id"], symb=symb)
        # Check if the user had already had shares of this business(symbol)
        if len(x) == 0:
            # If not add this business's information in the possession's table
            db.execute("INSERT INTO possession (user_id, symbole, name, ownedsharesnumber) VALUES(:Id, :symb, :name, :shar)",  Id=session["user_id"], symb=symb, name=dico["name"], shar=shar)
        else:
            # Otherwise update only the number of shares the user ownes
            db.execute("UPDATE possession SET ownedsharesnumber = :osn WHERE user_id = :Id AND symbole = :symb", Id=session["user_id"], symb=symb, osn=(OS[0]["ownedsharesnumber"] + shar))
        return redirect("/")

    else:
        return render_template("buy.html")





@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    H = db.execute("SELECT symbole, sharesnumber, price, orderdate, ordertime FROM history WHERE user_id = :Id", Id=session["user_id"])

    for row in H:
        row["price"] = usd(row["price"])


    return render_template("history.html", H=H)




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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        dico = dict()
        symbol = request.form.get("symbol")

        dico = lookup(symbol)
        if dico == None:
            return apology("INVALID SYMBOL", 400)

        return render_template("quoted.html", name=dico["name"], price=usd(dico["price"]), symbol=dico["symbol"])

    else:

        return render_template("quote.html")





@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Must provide a name", 400)
        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("Missing password", 400)
        # Ensure password = confirmation and  confirmation was submitted
        if request.form.get("password") != request.form.get("confirmation") or not request.form.get("confirmation"):
            return apology("Passwords don't match", 400)

        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        # Ensure this username doesn't already exist
        if len(rows) != 0:
            return apology("This username already exists")


        hashed = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)

        # Insert the new user's username and password in the database (in the table users)
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hashed)", username=request.form.get("username"), hashed=hashed)
        new = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        session["user_id"] = new[0]["id"]

        return redirect("/")


    else:
        return render_template("register.html")





@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":

        dico = dict()
        symb = request.form.get("symbol")
        shar = int(request.form.get("shares"))
        dico = lookup(symb)


        if not symb:
            return apology("MISSING SYMBOL", 400)

        if not shar:
            return apology("MISSING SHARES", 400)
        if shar < 1:
            return apology("VALUE MUST BE GREATER THAN OR EQUAL TO 1", 400)


        OSN = db.execute("SELECT ownedsharesnumber FROM possession WHERE user_id = :Id AND symbole = :symb", Id=session["user_id"], symb=symb)

        if OSN[0]["ownedsharesnumber"] == 0:
            return apology("NO SHARES OF THAT STOCK TO SELL", 400)

        if shar > OSN[0]["ownedsharesnumber"]:
            return apology("NOT ENOUGH SHARES OF THIS STOCK TO SELL", 400)


        usercash = db.execute("SELECT cash FROM users WHERE id = :Id", Id=session["user_id"])

        total = dico["price"] * shar


        db.execute("INSERT INTO history (user_id, symbole, name, price, sharesnumber, total, orderdate, ordertime) VALUES(:Id, :symb, :name, :price, :shar, :total, :date, :time)", Id=session["user_id"], symb=symb, name=dico["name"], price=dico["price"], shar= -shar, total=total, date=datetime.now().date(), time=datetime.now().time())

        db.execute("UPDATE users SET cash = :cash WHERE id = :Id", cash=(usercash[0]["cash"]+total), Id=session["user_id"])

        # number of share of this business(symbole) the user already possessed
        OS = db.execute("SELECT ownedsharesnumber FROM possession WHERE user_id = :Id AND symbole = :symb", Id=session["user_id"], symb=symb)


        # Otherwise update only the number of shares the user ownes
        db.execute("UPDATE possession SET ownedsharesnumber = :osn WHERE user_id = :Id AND symbole = :symb", Id=session["user_id"], symb=symb, osn=(OS[0]["ownedsharesnumber"] - shar))
        return redirect("/")


    else:

        S = db.execute("SELECT symbole FROM possession WHERE user_id = :Id AND ownedsharesnumber != 0", Id=session["user_id"])

        return render_template("sell.html", S=S)





def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
