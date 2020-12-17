from flask import  render_template, url_for, flash, redirect, request
from cardgame import app, db, bcrypt
from cardgame.forms import RegistrationForm, LoginForm
from cardgame.models import User
from cardgame import game_logic
from flask_login import login_user, current_user, logout_user, login_required

player_1_score, player_2_score, start = 0, 0, False

@app.route("/")
@app.route("/home")
def home():
    global start
    start = False

    return render_template("home.html", title="Home Page")


@app.route("/game")
def game():
    global start, player_1_score, player_2_score

    if not start:
        game_logic.set_game()

    start = True

    return render_template('game.html', player_1_score=player_1_score, player_2_score=player_2_score, title="Game Page")


@app.route("/roundend")
def game_results():
    global player_1_score, player_2_score

    data = game_logic.play()

    cycle, winner, player_1_score, player_2_score, player_1_card, player_2_card, game_winner = list(data[0].values())

    game_over = data[1]

    if game_over:
        return render_template("gameover.html", player_1_score=player_1_score, player_2_score=player_2_score,
                               game_winner=game_winner)

    return render_template("roundend.html", cycle=cycle, winner=winner, player_1_score=player_1_score,
                           player_2_score=player_2_score, player_1_card=', '.join(player_1_card),
                           player_2_card=', '.join(player_2_card), title="Round Results")


@app.route("/about")
def about():
    return render_template("about.html", title="About Page")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'An account has been created for user {form.username.data}! You can now login!', 'success')
        return redirect(url_for('home'))

    return render_template("register.html", title="Register", form=form)


@app.route("/account1")
def account1():
    return render_template("account1.html", title="Account Link 1")


@app.route("/account2")
def account2():
    return render_template("account2.html", title="Account Link 2")


@app.route("/account3")
def account3():
    return render_template("account3.html", title="Account Link 3")


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")