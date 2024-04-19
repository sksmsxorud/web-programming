from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello Root!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None);
    return {"item_id": item_id, "q": q}