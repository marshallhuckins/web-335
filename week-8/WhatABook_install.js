
// Drop existing database if it exists
db = db.getSiblingDB('WhatABook');
db.dropDatabase();

// Create and populate the customers collection
db.customers.insertMany([
    { _id: "c1001", firstName: "John", lastName: "Doe" },
    { _id: "c1002", firstName: "Jane", lastName: "Smith" }
]);

// Create and populate the books collection
db.books.insertMany([
    { _id: "b2001", title: "The Great Gatsby", genre: "Classic", author: "F. Scott Fitzgerald" },
    { _id: "b2002", title: "To Kill a Mockingbird", genre: "Fiction", author: "Harper Lee" }
]);

// Create and populate the wishlistItems collection
db.wishlistItems.insertMany([
    { _id: "w3001", customerId: "c1001", bookId: "b2001" },
    { _id: "w3002", customerId: "c1002", bookId: "b2002" }
]);

print("WhatABook database setup completed successfully.");
