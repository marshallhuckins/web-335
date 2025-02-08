"""
Author: Marshall Huckins
Date: 02/08/2025
File Name: Huckins_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand. 
It uses lists, loops, and conditionals to display tasks for each day.
"""

# List of tasks for running a lemonade stand
tasks = ["Buy lemons and sugar", "Prepare lemonade", "Set up the stand", "Sell lemonade", "Count earnings"]

# Using a for loop to print all tasks
print("Lemonade Stand Tasks:")
for task in tasks:
    print("-", task)  # Printing each task

print("\nWeekly Schedule:")

# List of days from Sunday to Saturday
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Using a for loop to iterate over days and assign tasks
for i in range(len(days)):
    if days[i] == "Saturday" or days[i] == "Sunday":
        print(f"{days[i]}: Day off - Time to rest!")
    else:
        print(f"{days[i]}: {tasks[i % len(tasks)]}")  # Assigning tasks in a loop
