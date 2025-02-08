/**
 * Huckins-HandsOn5.1.js
 * Author: Marshall Huckins
 * Date: 02/08/2025
 * Description: MongoDB Shell queries for Hands-On 5.1
 */

// (a) Add a new user
db.users.insertOne({
  "firstName": "Antonio",
  "lastName": "Vivaldi",
  "employeeId": "1013",
  "email": "avivaldi@me.com",
  "dateCreated": new Date()
});

// Verify user added
db.users.findOne({"email": "avivaldi@me.com"});

// (b) Update Mozart’s email
db.users.updateOne(
  { "email": "wmozart@me.com" },
  { $set: { "email": "mozart@me.com" } }
);

// Verify update
db.users.findOne({"email": "mozart@me.com"});

// (c) Display all users with projections
db.users.find({}, { "firstName": 1, "lastName": 1, "email": 1, "_id": 0 });
