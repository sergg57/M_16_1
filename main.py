# -*- coding: utf-8 -*-
from pyexpat.errors import messages

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_main_page():
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(user_id: int) -> dict:
    return {"messages":f'Вы вошли как пользователь № {user_id}'}

@app.get("/user")
async def user(username: str, age: int) -> dict:
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст {age}'}