''' Expensive Tracking App: A simple tool to track and organize your travel expenses on a daily basis'''


print("=" * 60)
print("                Travel Expense Tracking App")
print("=" * 60)

travel_day = int(input("\nDays on the road: "))
budget_amount = float(input("Total budget for the trip: "))
categories = ["lodging", "transportation" , "meals" , "other" ]
expense = []

print("Keep track of your expens: ")

# User add manually all expense for every category in every day
total_expense = 0
for day in range(travel_day): # for every day on travel days
    print(f"--- Expense for day {day + 1} ---") 
    expense_day = {}    # dictionary to which {"day 1": {"category": expense}} will be added
    total_day_expence = 0
    for category in categories:     # For each category in the category list      
        while True:    
            try:        
                amount = float(input(f"Insert the amount for {category}: ")) # Insert the amount of the category
                expense_day[category] = amount     # day[category] = add expense value
                total_day_expence += amount
                total_expense += amount
                break
            except ValueError:      # If I type something other than a number
                 print("Ivalid value, please check.")
    expense.append(expense_day)     # the dictionary with {"category" : expense} will be added to the expense list. Each dictionary is equivalent to one day
    print(f"Today you have spent: {total_day_expence:.2f}€")

print("total expense") # Calculate total daily spending by adding all categories


modify_expenses = input("You want to change some expenses? (y/n): ")

while modify_expenses.lower() == "y":
     day = int(input("Insert the day to modify (es. 1, 2, 3...): ")) - 1
     category = input("Enter the category to edit: ").lower()

     if day >= 0 and day < len(expense) and category in expense[day]:
        old_expense = expense[day][category]
        new_expense = float(input(f"Enter the new expense for {category} of the day {day + 1}: "))
        total_day_expence = total_day_expence - old_expense + new_expense
        total_expense = total_expense - old_expense + new_expense
        expense[day][category] = new_expense
        print("Modify correctly.")
        
        for i, day in enumerate(expense, 1):      # Recap expences in {day: categories} 
            print(f"Day {i}: {day}.")
                        
     else:
        print("Day or category wrong, try again")
     modify_expenses = input("Do you want to change other values? (y/n): ")



total_categories = {} # Sum of every expenses of all category
for day in expense:
    for category in categories:
        total_categories[category] = total_categories.setdefault(category, 0) + day[category]

print("\n--- TOTAL EXPENSE CATEGORIES ---")        
for category, total in total_categories.items():      
    print(f"- {category}: {total:.2f}€")
        
print(f"\nYou spent a total of: {total_expense:.2f}€")

remainder = budget_amount - total_expense
if remainder > 0:
     print(f"Available budget: {remainder:.2f}€\n")
elif remainder == 0:
     print("You've used up your entire budget for this trip\n")
else:  
     print(f"You went over budget for {abs(remainder):.2f}€\n")


print("*" * 60)
print("     Thanks for using this Travel Expense Tracking App")
print("*" * 60)
