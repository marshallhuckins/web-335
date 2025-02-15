"""
Title: Huckins_usersp1.py
Author: Marshall Huckins
Date: 02/15/25
Description: Python program to connect to MongoDB and perform user queries.
"""

# Import the MongoClient from pymongo
from pymongo import MongoClient

# Build a connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority", tlsAllowInvalidCertificates=True)

# Access the web335DB database
db = client['web335DB']

# ==========================
# Display all documents in the users collection
# ==========================
print("\n--- All Users in the Collection ---")
for user in db.users.find({}, {"firstName": 1, "lastName": 1, "_id": 0}):
    print(user)

# ==========================
# Find user by employeeId (1011)
# ==========================
print("\n--- User with Employee ID 1011 ---")
user_1011 = db.users.find_one({"employeeId": "1011"})
print(user_1011)

# ==========================
# Find user by lastName (Mozart)
# ==========================
print("\n--- User with Last Name 'Mozart' ---")
user_mozart = db.users.find_one({"lastName": "Mozart"})
print(user_mozart)
