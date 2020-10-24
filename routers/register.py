from flask import Blueprint, render_template, request
import random as r
from utils import hasher, DBHandler

routers = Blueprint("register", __name__)

@routers.route('/', methods=["GET", "POST"])
def register_route():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = str(request.form['username'])
        password = str(request.form['password'])
        email = str(request.form['email'])  

        hash = "#{}".format(r.randint(1000, 9999))
        username += hash

        password = hasher.hash(password)

        while 1:
            id = hasher.generateIdentifier(18)
            if DBHandler.isIdentifierAvailable(id):
                DBHandler.insertUser(username, password, email, id)
                break
        

        return render_template("index.html")


        