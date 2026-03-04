from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home", methods=["POST"])
def Home():
    number= request.form.get("number")
    
    if number == "123456":
        return render_template("home.html")
    
    else:
        return "Invalid Number"
    




if __name__ == "__main__":
    app.run(debug=True)