from flask import Blueprint
from flask import render_template

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template("home.html", title="Home Page")


@main.route("/about")
def about():
    return render_template("about.html", title="About Page")


@main.route("/help")
def user_help():
    return render_template("help.html", title="Card Game Help")
