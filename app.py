from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database

connection = mysql.connector.connect(user='root', host='127.0.0.1', database='gymsubs_flask')
cursor = connection.cursor()


def total_subscribers():
    """
    Get the number of subscribers
    """
    cursor.execute("SELECT COUNT(*) FROM subscribers")
    totalsubscribers = cursor.fetchone()[0]
    return totalsubscribers


def subscriber_exist(fn):
    """ See if a subscriber already exist """
    cursor.execute("SELECT * FROM subscribers WHERE firstname = :firstname", {"firstname": fn})
    if cursor.rowcount > 0:
        return True
    else:
        return False

# Routes


@app.route('/')
def index():
    """ Dashboard """
    return render_template("index.html", totalSubscribers=total_subscribers())


@app.route("/newsubscriber", methods=["POST"])
def newsubscriber():
    """ Add a new subscriber """

    #  Get info from html page

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    phone = request.form.get('phonenumber')
    email = request.form.get('email')
    creationdate = request.form.get('creationdate')
    expirationdate = request.form.get('expirationdate')

    if subscriber_exist(firstname) == True:
        return render_template("error.html", message="Subscriber already exist! Renew her/his subscription")
    else:
        return render_template("newsubscriber.html")


if __name__ == "__main__":
    app.run(debug=True)
