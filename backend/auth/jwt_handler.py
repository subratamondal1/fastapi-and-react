"""This module is responsible for signing, encoding, decoding and returning JWTS"""

# time is responsible for setting expiration time of the Tokens
import time  as _time
# jwt is responsible for encoding and decoding generated Tokens strings
import jwt as _jwt
# decouple helps you to organize your settings so that you can change the parameters without having to re-deploy your application, it also makes it easy to store parameters in inii or dotenv files
from decouple import config as _config

# for encoding and decoding
JWT_SECRET = str(_config("secret")) # reads from the .env file
# algorithm for encoding and decoding
JWT_ALGORITHM = str(_config("algorithm")) # reads from the .env file

def token_response(token:str):
    """Returns Generated Tokens (JWTs)"""
    return {
        "access_token": token
    }

def signJWT(userID:str):
    """Signing the JWT string"""
    payload = {
        "userID":userID,
        "expiry": _time.time() + 600
    }
    token = _jwt.encode(
        payload=payload,
        key = JWT_SECRET,
        algorithm=JWT_ALGORITHM
    )
    return token_response(token=token)

def decodeJWT(token:str):
    try:
        decode_token = _jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decode_token if decode_token["expiry"] >= _time.time() else None
    except:
        return {}