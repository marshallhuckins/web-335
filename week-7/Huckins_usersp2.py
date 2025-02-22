"""
Title: Huckins_usersp2.py
Author: Marshall Huckins
Date: 21 February 2025
Description: This script connects to the web335DB database on MongoDB Atlas and performs CRUD operations:
             1. Inserts a new user document.
             2. Retrieves the document to prove it was created.
             3. Updates the user's email address.
             4. Retrieves the document to prove the update.
             5. Deletes the document.
             6. Verifies that the document has been deleted.
"""

from pymongo import MongoClient
import datetime

# Use the working connection string from last week
connection_string = "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"

# Build a connection to MongoDB Atlas with tlsAllowInvalidCertificates enabled
client = MongoClient(connection_string, tlsAllowInvalidCertificates=True)

# Access the web335DB database
db = client['web335DB']

# ---------------------------
# 1. Create a new user document
# ---------------------------
new_user = {
    "firstName": "Marshall",
    "lastName": "Huckins",
    "employeeId": "1013",
    "email": "marshall.huckins@example.com",
    "dateCreated": datetime.datetime.now(datetime.timezone.utc)
}

# Insert the document into the users collection and capture the inserted_id
inserted_id = db.users.insert_one(new_user).inserted_id
print("Inserted Document ID:", inserted_id)

# ---------------------------
# 2. Prove the document was created
# ---------------------------
created_user = db.users.find_one({"employeeId": "1013"})
print("Created Document:", created_user)

# ---------------------------
# 3. Update the email address of the created document
# ---------------------------
update_result = db.users.update_one(
    {"employeeId": "1013"},
    {"$set": {"email": "marshall.updated@example.com"}}
)

# ---------------------------
# 4. Prove the document was updated
# ---------------------------
updated_user = db.users.find_one({"employeeId": "1013"})
print("Updated Document:", updated_user)

# ---------------------------
# 5. Delete the document
# ---------------------------
delete_result = db.users.delete_one({"employeeId": "1013"})
print("Delete Result:", delete_result)

# ---------------------------
# 6. Prove the document was deleted
# ---------------------------
deleted_user = db.users.find_one({"employeeId": "1013"})
print("Document after deletion (should be None):", deleted_user)
