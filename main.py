from flask import Flask, render_template, request, send_file


from routers.register import routers
from routers.login import login

app = Flask(__name__)



# ROUTES
app.register_blueprint(routers, url_prefix="/register")
app.register_blueprint(login, url_prefix="/login")

@app.route('/', methods=["GET"])
def index_route():
    return render_template('index.html')

@app.route('/mailinglist', methods=["GET"])
def mailing_route():
    return render_template("mailing.html")
    
@app.route('/joinml', methods=["POST"])
def joinml_route():
    form_data = request.form["email"]
    email = form_data

    # TODO: add to mailing list.
    file = open("emails.txt", "a")
    
    file.write(email + "\n")
    return render_template("status.html", st="Woohoo! You've joined the mailing list. You will be redirected in a second!")
    
    #return 'OK'

@app.route('/background', methods=["GET"])
def background_route():
    return send_file('templates/background.png', mimetype="image/gif")

@app.route('/inquires', methods=["GET"])
def inquires_route():
    return render_template("inquiries.html")
if __name__ == "__main__":
    app.run(debug=True)
