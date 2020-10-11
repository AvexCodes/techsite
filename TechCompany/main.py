from flask import Flask, render_template, request

app = Flask(__name__)

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


@app.route('/inquires', methods=["GET"])
def inquires_route():
    return render_template("inquiries.html")
if __name__ == "__main__":
    app.run(debug=True, host='192.168.0.38')
