
#!/usr/bin/python3
"""
flask webframe work
"""


from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def index2():
    return "HBNB"


@app.route("/c/<text>")
def index3(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def display(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>/")
def integer_req(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>/")
def serve_page(n):
    return render_template("templates/5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>/")
def det_serve_pg(n):
    if n % 2 == 0:
        catg = "even"
    else:
        catg = "odd"
    return render_template("6-number_odd_or_even.html",
                            n=n, catg=catg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
