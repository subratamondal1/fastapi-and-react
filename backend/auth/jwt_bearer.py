"""The function of this module is to check whether the request is authorized or not [Verification of the Protected Route]"""

import fastapi as _fastapi
import fastapi.security as _security

import jwt_handler as _jwt_handler

class JwtBearer(_security.HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_Error)

    async def __call__(self, request: _fastapi.Request):
        credentials: _security.HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise _fastapi.HTTPException(
                    status_code=_fastapi.status.HTTP_403_FORBIDDEN,
                    detail="Invalid or Expired Token"
                )
            return credentials.credentials
        return _fastapi.HTTPException(
                    status_code=_fastapi.status.HTTP_403_FORBIDDEN,
                    detail="Invalid or Expired Token"
                )
    def verify_jwt(self, jwtoken:str):
        isTokenValid:bool = False
        payload = _jwt_handler.decodeJWT(token=jwtoken)
        if payload:
            isTokenValid=True
        return isTokenValid