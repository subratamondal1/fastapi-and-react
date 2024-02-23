"""Entry Point"""

import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services as _services
import schemas as _schemas

app = _fastapi.FastAPI()

@app.post(path="/api/users")
async def create_user(user:_schemas.UserCreate, db:_orm.Session=_fastapi.Depends(_services.get_db)):
    db_user = await _services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise _fastapi.exceptions.HTTPException(
            status_code=_fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Email already exists!!!"
        )
    return await _services.create_user(user=user, db=db)

if __name__ == "__main__":
    import uvicorn as _uvicorn
    _uvicorn.run(app="main:app", port=8000, reload=True)