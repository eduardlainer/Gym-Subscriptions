from flask import Flask, render_template, request
import database

app = Flask(__name__)

# Database

db = database.Database()


# Routes


@app.route('/')
def index():
    """ Dashboard """
    return render_template("index.html", totalSubscribers=db.total_subscribers(),
                           activeSubs=db.totalactivesubscription(), expiredSubs=db.totalexpiredsubscription())


@app.route('/newsubscription')
def newsubscription():
    """ new subscription page """
    return render_template("newsubscription.html")


@app.route('/existingsubscriber')
def existingsubscriber():
    """ existing subscription page """
    return render_template("existingsubscriber.html", subscribers=db.getsubscribers())


@app.route('/checksubscription')
def checksubscription():
    """ subscription status page """
    return render_template("checksubscription.html")


# Resolving routes


@app.route('/checksub', methods=['POST', 'GET'])
def checksub():
    """
    Check subscription status
    """

    #  Get info from form

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')

    # Check subscription

    subcheck = db.checksubscription(firstname, lastname)
    subexist = db.subscriber_exist(firstname, lastname)
    if subexist is False:
        return render_template('/error.html', message="Subscriber doesn't exist!")

    subcheckalert = db.checksubscriptionalert(firstname, lastname)
    if subcheckalert == 1:
        message = "Subscription expired!"
        classalert = "alert-danger"
    else:
        message = "Subscription is ok"
        classalert = "alert-success"
    return render_template('/checksubscription.html', subcheck=subcheck, message=message, classalert=classalert)


@app.route('/existingsub', methods=['POST', 'GET'])
def existingsub():
    """
    Renew an subscription of an old suberiber
    """

    # Get info from form

    subscriber_id = int(request.form.get('subscriber_id'))
    creationdate = request.form.get('creationdate')
    expirationdate = request.form.get('expirationdate')

    # Renew subscription

    db.renewsubscription(subscriber_id, creationdate, expirationdate)
    return render_template("success.html", message="Subscription renewed!")



@app.route("/newsubscriber", methods=['POST', 'GET'])
def newsubscriber():
    """ Add a new subscriber """

    #  Get info from form

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    phone = request.form.get('phonenumber')
    email = request.form.get('email')
    creationdate = request.form.get('creationdate')
    expirationdate = request.form.get('expirationdate')

    # Check if subscriber already exist

    if db.subscriber_exist(firstname, lastname):
        return render_template("error.html",
                               message="Subscriber already exist! Got to existing subscribers and renew the subsciption.")

    # If subscriber doesn't exist add

    db.addsubscriber(firstname, lastname, phone, email, creationdate, expirationdate)
    return render_template("success.html", message="You added a new subscription.")


if __name__ == "__main__":
    app.run(debug=True)
