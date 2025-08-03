from fastapi import FastAPI, Body
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def get_books():
    with open("books.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    with open('books.json', 'r') as file:
        data = json.load(file)
    books = data["books"]
    for book in books:
        if book['id'] == book_id:
            return book
    return "Book was not found"

@app.get("/books/")
async def get_book_by_genre_Query(genre: str):
    with open('books.json', 'r') as file:
        data = json.load(file)
    books = data["books"]
    books_to_return = []
    for book in books:
        if book['genre'].casefold() == genre.casefold():
            books_to_return.append(book)       
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book: dict = Body()):
    with open('books.json', 'r') as file:
        data = json.load(file)
    
    books = data["books"]
    
    # Generate a new ID (assuming IDs are sequential)
    new_id = max(book['id'] for book in books) +1    
    new_book['id'] = new_id
    
    books.append(new_book)
    data["books"] = books
    
    with open('books.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return {"message": "Book created successfully", "book": new_book}
    




