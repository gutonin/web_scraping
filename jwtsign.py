import jwt
import time
from fastapi import HTTPException
import  secrets

JWT_SECRET = secrets.token_hex
JWT_ALG = 'HS256'

print(JWT_SECRET)

def sign(email):
    payload = {'email': email}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
    return token

def decode(token):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=[JWT_ALG])
        return decoded_token
    except:    
        raise HTTPException(status_code=401, detail='Token invalido')