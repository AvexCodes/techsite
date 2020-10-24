import hashlib
import string
import random

def hash(password: str):
   return hashlib.sha512(bytes(password, "utf-8")).hexdigest()

def generate_session(r: int):
    alphabet = string.ascii_letters + "123456789"
    return ''.join(random.choice(alphabet) for i in range(r))

def generateIdentifier(r: int):
    alphabet = "1234567890"
    return ''.join(random.choice(alphabet) for i in range(r))