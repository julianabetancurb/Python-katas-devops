from fastapi import FastAPI
from pydantic import BaseModel
from src.dictionary import Dictionary
from src.costs import get_total
from src.concatenate import concatenate
from mangum import Mangum
app = FastAPI(title="Python Katas API", root_path="/prod")


dict_store = Dictionary()

class DictEntry(BaseModel):
    word: str
    definition: str

@app.post("/dictionary/new-entry")
def add_entry(entry: DictEntry):
    dict_store.newentry(entry.word, entry.definition)
    return {"message": f"Added word '{entry.word}' successfully."}

@app.get("/dictionary/look/{word}")
def look_entry(word: str):
    return {"definition": dict_store.look(word)}


class ShoppingCart(BaseModel):
    costs: dict
    items: list
    tax: float

@app.post("/shopping/total")
def calculate_total(cart: ShoppingCart):
    total = get_total(cart.costs, cart.items, cart.tax)
    return {"total": total}


class WordList(BaseModel):
    words: list

@app.post("/words/concatenate")
def get_concatenate(data: WordList):
    return {"result": concatenate(data.words)}

handler = Mangum(app, lifespan="off")