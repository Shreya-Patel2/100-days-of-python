from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap4


app = Flask(__name__)
app.secret_key = "###"
bootstrap = Bootstrap4(app)


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8,
                                                                                  message="Field must be at least 8 characters long.")])
    submit = SubmitField(label='Log In')
    csrf_token = app.secret_key


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == "###" and form.password.data == "###":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
