from pymongo import MongoClient

def connect_db():
    """Establish connection to MongoDB and handle connection errors."""
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)  # 3-second timeout
        db = client["WhatABook"]
        # Force a server check
        client.admin.command("ping")
        return db
    except Exception as e:
        print("Error: Could not connect to MongoDB. Is the database running?")
        return None

def list_books(db):
    """Display all books in the database."""
    books = db.books.find()
    for book in books:
        print(f"{book['_id']}: {book['title']} by {book['author']} ({book['genre']})")

def search_books_by_genre(db, genre):
    """Search books by genre."""
    books = db.books.find({"genre": {"$regex": f"^{genre}$", "$options": "i"}})
    for book in books:
        print(f"{book['_id']}: {book['title']} by {book['author']}")

def search_books_by_author(db, author):
    """Search books by author."""
    books = db.books.find({"author": {"$regex": f"^{author}$", "$options": "i"}})
    for book in books:
        print(f"{book['_id']}: {book['title']} ({book['genre']})")

def search_book_by_id(db, book_id):
    """Search for a book by bookId."""
    book = db.books.find_one({"_id": book_id})
    if book:
        print(f"{book['_id']}: {book['title']} by {book['author']} ({book['genre']})")
    else:
        print("Book not found.")

def view_wishlist(db, customer_id):
    """Retrieve and display a customer's wishlist."""
    if not db.customers.find_one({"_id": customer_id}):
        print("Invalid customer ID.")
        return
    
    wishlist_items = db.wishlistItems.find({"customerId": customer_id})
    if db.wishlistItems.count_documents({"customerId": customer_id}) == 0:
        print("No books found in wishlist.")
        return
    
    for item in wishlist_items:
        book = db.books.find_one({"_id": item["bookId"]})
        if book:
            print(f"{book['_id']}: {book['title']} by {book['author']} ({book['genre']})")
        else:
            print("Book not found.")

def add_book_to_wishlist(db, customer_id, book_id):
    """Add a book to a customer's wishlist."""
    if not db.customers.find_one({"_id": customer_id}):
        print("Invalid customer ID.")
        return
    if not db.books.find_one({"_id": book_id}):
        print("Invalid book ID.")
        return
    
    db.wishlistItems.insert_one({"customerId": customer_id, "bookId": book_id})
    print("Book successfully added to wishlist.")

def remove_book_from_wishlist(db, customer_id, book_id):
    """Remove a book from a customer's wishlist."""
    result = db.wishlistItems.delete_one({"customerId": customer_id, "bookId": book_id})
    if result.deleted_count > 0:
        print("Book successfully removed from wishlist.")
    else:
        print("Book not found in wishlist.")

def main():
    db = connect_db()
    if db is None:
        return
    
    while True:
        print("\nWhatABook Menu")
        print("1. List all books")
        print("2. Search books by genre")
        print("3. Search books by author")
        print("4. Search book by ID")
        print("5. View wishlist")
        print("6. Add book to wishlist")
        print("7. Remove book from wishlist")
        print("8. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            list_books(db)
        elif choice == "2":
            genre = input("Enter genre: ")
            search_books_by_genre(db, genre)
        elif choice == "3":
            author = input("Enter author: ")
            search_books_by_author(db, author)
        elif choice == "4":
            book_id = input("Enter book ID: ")
            search_book_by_id(db, book_id)
        elif choice == "5":
            customer_id = input("Enter customer ID: ")
            view_wishlist(db, customer_id)
        elif choice == "6":
            customer_id = input("Enter customer ID: ")
            book_id = input("Enter book ID: ")
            add_book_to_wishlist(db, customer_id, book_id)
        elif choice == "7":
            customer_id = input("Enter customer ID: ")
            book_id = input("Enter book ID: ")
            remove_book_from_wishlist(db, customer_id, book_id)
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
