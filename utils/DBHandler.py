import mysql.connector
import utils.hasher as hasher

from dateutil.parser import parse

from datetime import timedelta, datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vexdb"
)

cursor = db.cursor()

def insertUser(username: str, password: str, email: str, id: str):
    sql = """
            INSERT INTO accounts(username, email, password, identifier) VALUES (%s, %s, %s, %s)
          """

    values = (username, email, password, id)
    cursor.execute(sql, values)
    db.commit()

def isIdentifierAvailable(id: str):
    sql = """
            SELECT * FROM accounts WHERE identifier = '%s' 

          """
    values = (id)
    cursor.execute(sql, values)
    res = cursor.fetchone()

    if res is None:
        return True

    return False


def login(email: str, password: str):
    email.replace("'", "")
    email.replace('"', "")
    sql = "SELECT * FROM `accounts` WHERE email = %s"

    cursor.execute(sql, (email,))

    res = cursor.fetchone()
    return res or None

def generate_session_id(identifier: str):
    session_id = hasher.generate_session(6)
    old = session_id
    print(session_id)
    session_id = hasher.hash(session_id)
    expiry = datetime.now() + timedelta(days=14)
    sql = "INSERT INTO sessions(sessionId, identifier, date) VALUES(%s, %s, %s)"

    cursor.execute(sql, (session_id, identifier, expiry))
    db.commit()
    return old

def check_session(session_id: str):
    session_id = hasher.hash(session_id)
    sql = "SELECT * FROM `sessions` WHERE sessionId = %s"
    cursor.execute(sql, (session_id,))
    res = cursor.fetchone()

    if res is None:
        return False

    if datetime.now > datetime.strptime(res[3], "%y-%m-%d %H:%M:%S.%f"):
        return False
    
    return True

def get_session_credentials(session_id: str):
    sql = "SELECT * FROM `sessions` WHERE sessionId = %s"
    cursor.execute(sql, (session_id,))
    res = cursor.fetchone()

    return res

    