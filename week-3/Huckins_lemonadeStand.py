"""
Author: Marshall Huckins
Date: 01/20/2025
File Name: Huckins_lemonadeStand.py
Description: This file gives examples on how to build functions and emulates a lemonade stand.
"""

# Create function to calculate total cost
def calculate_cost(lemons_cost, sugar_cost):
  return lemons_cost + sugar_cost

# Create function to calculate profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
  total_cost = calculate_cost(lemons_cost, sugar_cost)
  return selling_price - total_cost

# get input from user and assign to variables
lemons_cost = float(input("What is the cost of lemons? "))
sugar_cost = float(input("What is the cost of sugar? "))
selling_price = float(input("How much is it selling for? "))

# Calculate total cost and profit
total_cost = calculate_cost(lemons_cost, sugar_cost)
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Print results to console
print(f"Cost of lemons: ${lemons_cost} + Cost of Sugar: ${sugar_cost} = Total cost: ${total_cost}")
print(f"Selling price: ${selling_price} - Total cost: ${total_cost} = Profit: ${profit}")