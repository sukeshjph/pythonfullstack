from fastapi import FastAPI, Body
import json

app = FastAPI()

def getBooksFromjson():
    with open("books.json", "r") as file:
        data = json.load(file)
    return data["books"]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def get_books():
    books = getBooksFromjson()
    return books

@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    books = getBooksFromjson()
    for book in books:
        if book['id'] == book_id:
            return book
    return "Book was not found"

@app.get("/books/")
async def get_book_by_genre_Query(genre: str):
    books = getBooksFromjson()
    books_to_return = []
    for book in books:
        if book['genre'].casefold() == genre.casefold():
            books_to_return.append(book)       
    return books_to_return

@app.post("/books/create_book")
async def create_book(new_book: dict = Body()):
    books = getBooksFromjson()
    # Generate a new ID (assuming IDs are sequential)
    new_id = max(book['id'] for book in books) +1    
    new_book['id'] = new_id
    
    books.append(new_book)

    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)
    
    return {"message": "Book created successfully", "book": new_book}

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    books = getBooksFromjson()
    for i in range(len(books)):
        if books[i].get('title').casefold() == updated_book.get('title').casefold():
            books[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    books = getBooksFromjson()
    for i in range(len(books)):
        if books[i].get('title').casefold() == book_title.casefold():
            books.pop(i)
            break
    




