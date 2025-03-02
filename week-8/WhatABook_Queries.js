
// Switch to the WhatABook database
db = db.getSiblingDB('WhatABook');

// Query 1: Display a list of all books
print("All Books:");
printjson(db.books.find().toArray());

// Query 2: Display a list of books by genre (Example: 'Fiction')
print("Books in Genre - Fiction:");
printjson(db.books.find({ genre: "Fiction" }).toArray());

// Query 3: Display a list of books by author (Example: 'Harper Lee')
print("Books by Harper Lee:");
printjson(db.books.find({ author: "Harper Lee" }).toArray());

// Query 4: Display a book by bookId (Example: 'b2001')
print("Book with ID b2001:");
printjson(db.books.findOne({ _id: "b2001" }));
