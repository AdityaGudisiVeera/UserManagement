from model import User
from fastapi import FastAPI

#data
users =[
    User(id=1,name="Aditya",age=40,relation=True,gender="Male"),
]
#FASTAPI is a class So we create instance
app=FastAPI()
#routes 
@app.get("/")
async def homepage():
    return {"message":"welcome to fastapi"}

@app.get("/users")
async def user_info():
    return users


# create new user
@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return {"message":f"new user created successfully {user}"}


#specific user
@app.get("/users/{id}")
async def specific_user(id:int):
    for user in users:
        if user.id == id:
            return user
    return {"error":f"user doesnot found of {id}"}


#updating the user
@app.put("/users/{id}")
async def update_user(id:int,user:User):
    for i in range(len(users)):
        if users[i].id == id:
            users[i] = user
            return {"message":f"user data is updated {user}"}
    return{"error:failed to update"}


#delete the user
@app.delete("/users/{id}")
async def delete_user(id:int):
    for i in range(len(users)):
        if users[i].id == id:
            users.pop(i)
            return {"Successfully deleted"}
    return {"error: failed to delete"}