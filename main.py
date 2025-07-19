from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Модель животного
class Animal(BaseModel):
    name: str
    species: str
    age: int

# Хранилище в памяти
db: Dict[int, Animal] = {}
counter = 1

# Create
@app.post("/animals")
def create_animal(animal: Animal):
    global counter
    db[counter] = animal
    counter += 1
    return {"id": counter - 1, "animal": animal}

# Read all
@app.get("/animals")
def list_animals():
    return db

# Read one
@app.get("/animals/{animal_id}")
def get_animal(animal_id: int):
    if animal_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    return db[animal_id]

# Update
@app.put("/animals/{animal_id}")
def update_animal(animal_id: int, animal: Animal):
    if animal_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    db[animal_id] = animal
    return {"id": animal_id, "animal": animal}

# Delete
@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    if animal_id not in db:
        raise HTTPException(status_code=404, detail="Not found")
    del db[animal_id]
    return {"message": "Deleted"}
-