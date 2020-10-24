from flask import Blueprint, render_template, request, make_response, redirect
from utils import DBHandler, hasher
login = Blueprint("login", __name__)

@login.route('/', methods=["GET", "POST"])
def login_route():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        email = str(request.form['email'])
        password = hasher.hash(str(request.form['password']))

        result = DBHandler.login(email, password)

        #return "{}".format(res, email, password)

        if request.cookies.get('session_id') is not None:
            validate = DBHandler.check_session(request.cookies.get('session_id'))
            print(validate)
            if validate == True:
                return redirect("/")

        if result is None:
            return render_template("login.html")
        if result[3] == password:
            #return "bababooey"
            res = make_response(render_template("status.html", st="Successfully logged in! you will redirected in a second!"))
            session_id = DBHandler.generate_session_id(result[4])
            res.set_cookie("session_id", session_id)
            return res
        else:
            return render_template("login.html  ")