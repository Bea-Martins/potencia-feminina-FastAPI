from fastapi import FastAPI, HTTPException
from typing import List
from models import User,Role
from  uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
  User(id=UUID("9700c111-8da5-4e1b-8e78-c609f914302b"), first_name='Ana', last_name='Maria', email='email@gmail.com', role=[Role.role_1]), 
  User(id=UUID("b77694fb-ad13-42db-83b3-c28da9da337e"), first_name='Cynthia', last_name='Zanoni', email='cynthia@gmail.com', role=[Role.role_3]), 
  User(id=UUID("f9b37758-a47c-4327-b2c0-64a997cb2938"), first_name='Bea', last_name='Martins', email='bea@gmail.com', role=[Role.role_2]), 
]

@app.get("/")
async def root():
  return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
  return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
  for user in db:
    if user.id == id:
      return user
  return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
  for user in db:
    if user.id == id:
      db.remove(user)
      return
  raise HTTPException(
    status_code=404,
    detail=f"Usuário com o id {id} não encontrado!"
  )