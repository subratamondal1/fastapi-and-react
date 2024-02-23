"""Entry Point"""
import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services as _services
import schemas as _schemas

import models as _models
import auth.jwt_handler as _jwt_handler
import auth.jwt_bearer as _jwt_bearer

posts = [
    {
        "id":1,
        "title": "penguin 🐧",
        "content": "penguins are group of...."
    },
    {
        "id":2,
        "title": "tiger 🐯",
        "content": "tigers are group of...."
    },
    {
        "id":3,
        "title": "snake 🐍",
        "content": "snakes are group of...."
    },
]

users = []

app = _fastapi.FastAPI()

@app.get(path="/", tags=["test"])
def greet():
    return {"Hello":"World"}

# get all posts
@app.get(path="/posts", tags=["posts"])
def get_all_posts():
    return {"data":posts}

# get single post by id
@app.get(path=f"/posts/{id}", tags=["posts"])
def get_one_post(id:int):
    if id > len(posts):
        return _fastapi.exceptions.HTTPException(
            status_code=_fastapi.status.HTTP_400_BAD_REQUEST,
            detail="Id doesn't exists..."
        )
    for post in posts:
        if post["id"] == id:
            return {
                "data":post
            }
# create a new user
@app.post(path="/user/signup", tags=["user"])
def user_signup(user:_models.UserSchema = _fastapi.Body(default=None)):
    users.append(user)
    return _jwt_handler.signJWT(userID=user.email)

def check_user_existence(data:_models.UserLoginSchema):
    for user in users:
        if (user.email == data.email) and (user.password == data.password):
            return True
        return False

@app.post(path="/user/signin", tags=["user"])
def user_login(user:_models.UserLoginSchema=_fastapi.Body(default=None)):
    if check_user_existence(user):
        return _jwt_handler.signJWT(userID=user.email)
    return _fastapi.exceptions.HTTPException(
        status_code=_fastapi.status.HTTP_400_BAD_REQUEST,
        detail="Invalid Credentials"
    )

@app.post(path="/posts", dependencies=[_fastapi.Depends(_jwt_bearer.JwtBearer())], tags=["posts"])
def add_post(post: _models.PostSchema):
    post.id = len(posts) + 1
    posts.append(post.model_dump())
    return {
        "info": "Post Added"
    }
    

if __name__ == "__main__":
    import uvicorn as _uvicorn
    _uvicorn.run(app="main:app", port=8000, reload=True)