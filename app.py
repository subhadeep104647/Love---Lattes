from flask import Flask, render_template, request, redirect, url_for, session
import json
from flask import flash

app = Flask(__name__)
app.secret_key = "love_lattes_secret"


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
    cart_count = len(session.get("cart", []))
    return render_template("menu.html", cart_count=cart_count)


# ADD ITEM TO CART
@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():

    item = request.form.get("item")
    price = int(request.form.get("price"))

    if "cart" not in session:
        session["cart"] = []

    session["cart"].append({
        "item": item,
        "price": price
    })

    session.modified = True

    return redirect(url_for("menu"))


# VIEW CART
@app.route("/cart")
def cart():

    cart_items = session.get("cart", [])

    total = sum(item["price"] for item in cart_items)

    return render_template("cart.html", cart=cart_items, total=total)


# REMOVE ITEM
@app.route("/remove/<int:index>")
def remove(index):

    cart = session.get("cart", [])

    if 0 <= index < len(cart):
        cart.pop(index)
        session["cart"] = cart
        session.modified = True

    return redirect(url_for("cart"))

# PLACE ORDER
@app.route("/order")
def order():

    session.pop("cart", None)

    flash("🎉 Order placed successfully! Your Order is on the way, Thank you ")
    return redirect(url_for("cart"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/Feedback")
def Feedback():
    return render_template("feedback.html")

@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    feedback_data = {
        "name": name,
        "email": email,
        "message": message
    }

    try:
        with open("feedback.json","r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(feedback_data)

    with open("feedback.json","w") as file:
        json.dump(data,file,indent=4)

    flash("Thank you for your feedback ☕")
    return redirect(url_for("Feedback"))


if __name__ == "__main__":
    app.run(debug=True)