# Project: Expense Tracker - Installment 2
# Author: Danilo Ehmiel C. Esmeralda
# Description: Asks the user for two expenses and calculates the total and average.

print("=" * 40)

print("\tEXPENSE TRACKER")
print("\tKnow where your money goes.")

print("=" * 40)

print("MAIN MENU")
print(f"\t{'[1] Add an expense'.ljust(34)}(coming soon)")
print(f"\t{'[2] View all expenses'.ljust(34)}(coming soon)")
print(f"\t{'[3] Show total spent'.ljust(34)}(coming soon)")
print(f"\t{'[4] Exit'.ljust(34)}(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("First expense? ")
amount1 = float(input("Amount? "))

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))

total = amount1 + amount2
average = total / 2

print("-" * 40)
print("SUMMARY")
print(f"\t- {item1}:\t${amount1}")
print(f"\t- {item2}:\t${amount2}")
print(f"Total spent:\t${total}")
print(f"Average:\t${average}")
print("-" * 40)

print(f"Made by: Danilo Ehmiel C. Esmeralda | Installment 2")