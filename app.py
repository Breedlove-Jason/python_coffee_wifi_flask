from flask import Flask, render_template, redirect, url_for, flash
import os
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from form import CafeForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Bootstrap(app)
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    open_time = db.Column(db.String(100), nullable=False)
    close_time = db.Column(db.String(100), nullable=False)
    coffee_rating = db.Column(db.String(10), nullable=False)
    wifi_rating = db.Column(db.String(10), nullable=False)
    power_rating = db.Column(db.String(10), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    cafes = Cafe.query.all()
    return render_template("index.html", cafes=cafes)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.name.data,
            location=form.location.data,
            open_time=form.open_time.data,
            close_time=form.close_time.data,
            coffee_rating=form.coffee_rating.data,
            wifi_rating=form.wifi_rating.data,
            power_rating=form.power_rating.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        flash("Cafe added successfully!", "success")
        return redirect(url_for("home"))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
