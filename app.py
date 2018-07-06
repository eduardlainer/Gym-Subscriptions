from flask import Flask, render_template, request
import database

app = Flask(__name__)

# Database

db = database.Database()

# Routes


@app.route('/')
def index():
    """ Dashboard """
    return render_template("index.html", totalSubscribers=db.total_subscribers())


@app.route('/newsubscription', methods=['POST', 'GET'])
def newsubscription():
    """ Add a new subscription page """
    return render_template("newsubscription.html")


@app.route("/newsubscriber", methods=['POST', 'GET'])
def newsubscriber():
    """ Add a new subscriber """

    #  Get info from html page

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    phone = request.form.get('phonenumber')
    email = request.form.get('email')
    creationdate = request.form.get('creationdate')
    expirationdate = request.form.get('expirationdate')

    if db.subscriber_exist(firstname):
        return render_template("error.html",
                               message="Subscriber already exist! Got to existing subscribers and renew the subsciption.")

    db.addsubscriber(firstname, lastname, phone, email, creationdate, expirationdate)
    return render_template("succes.html", message="You added a new subscription.")


if __name__ == "__main__":
    app.run(debug=True)
