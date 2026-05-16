from fastapi import FastAPI
from pydantic import BaseModel
from src.dictionary import Dictionary
from src.costs import get_total
from src.concatenate import concatenate

app = FastAPI(title="Python Katas API")

# --------- Kata 1: Dictionary ---------
dict_store = Dictionary()

class DictEntry(BaseModel):
    word: str
    definition: str

@app.post("/dictionary/new-entry")
def add_entry(entry: DictEntry):
    dict_store.newentry(entry.word, entry.definition)
    return {"message": f"Added {entry.word}"}

@app.get("/dictionary/look/{word}")
def look_entry(word: str):
    return {"definition": dict_store.look(word)}

# --------- Kata 2: Shopping total ---------
class ShoppingCart(BaseModel):
    costs: dict
    items: list
    tax: float

@app.post("/shopping/total")
def calculate_total(cart: ShoppingCart):
    total = get_total(cart.costs, cart.items, cart.tax)
    return {"total": total}

# --------- Kata 3: Nth character ---------
class WordList(BaseModel):
    words: list

@app.post("/words/concatenate")
def get_concatenate(data: WordList):
    return {"result": concatenate(data.words)}