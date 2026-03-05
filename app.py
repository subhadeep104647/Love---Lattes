from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/home", methods=["GET","POST"])
def home():
    if request.method == "POST":
        number = request.form.get("number")

        if number == "123456":
            return render_template("home.html")
        else:
            return "Invalid Number"
    else:
        return render_template("home.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)