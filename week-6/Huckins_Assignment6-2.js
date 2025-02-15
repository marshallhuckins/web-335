/**
 * Title: Huckins-Assignment6.js
 * Author: Marshall Huckins
 * Date: [Insert Date]
 * Description: MongoDB Queries for Houses and Students Collections
 */

// ==========================
// STEP 1: Display All Students
// ==========================
db.students.find().pretty();

// ==========================
// STEP 2: Add a New Student
// ==========================
db.students.insertOne({
   "firstName": "Marshall",
   "lastName": "Huckins",
   "studentId": "s1019",
   "houseId": "h1008",
   "wand": "Oak, 12 inches, Phoenix Feather",
   "patronus": "Badger"
});

// Verify student was added
db.students.find({ "firstName": "Marshall", "lastName": "Huckins" }).pretty();

// ==========================
// STEP 3: Update the Student's Patronus
// ==========================
db.students.updateOne(
   { "firstName": "Marshall", "lastName": "Huckins" },
   { $set: { "patronus": "Otter" } }
);

// Verify the update
db.students.find({ "firstName": "Marshall", "lastName": "Huckins" }).pretty();

// ==========================
// STEP 4: Delete the Student
// ==========================
db.students.deleteOne({ "firstName": "Marshall", "lastName": "Huckins" });

// Verify student was removed
db.students.find({ "firstName": "Marshall", "lastName": "Huckins" }).pretty();

// ==========================
// STEP 5: Display All Students by House
// ==========================
db.students.aggregate([
   { $lookup: {
       from: "houses",
       localField: "houseId",
       foreignField: "houseId",
       as: "houseDetails"
   }},
   { $unwind: "$houseDetails" },
   { $group: {
       _id: "$houseDetails.houseId",
       houseName: { $first: "$houseDetails.founder" },
       students: { $push: "$firstName" }
   }}
]);

// ==========================
// STEP 6: Display All Students in Gryffindor
// ==========================
db.students.find({ "houseId": "h1007" }).pretty();

// ==========================
// STEP 7: Display All Students in the House with an Eagle Mascot
// ==========================

// Get the houseId for the house with an Eagle mascot
var eagleHouse = db.houses.findOne({ "mascot": "Eagle" }).houseId;

// Display students in that house
db.students.find({ "houseId": eagleHouse }).pretty();
