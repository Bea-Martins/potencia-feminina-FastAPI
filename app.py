from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None

@app.get("/")
async def root():
  return {"message": "Olá, WoMakers!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, busca: Union[str, int] = None):
  return {"item_id": item_id, "busca": busca}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
  return {"item_name": item.name, "item_id": item_id}