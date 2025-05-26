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
for day in range(1,travel_day + 1): # for every day on travel days
    print(f"--- Expense for day {day} ---") 
    expense_day = {}    # dictionary to which {"day 1": {"category": expense}} will be added
    for category in categories:     # For each category in the category list
        
        while True:    
            try:        
                amount = float(input(f"Insert the amount for {category}: ")) # Insert the amount of the category
                expense_day[category] = amount     # day[category] = add expense value
                break
            except ValueError:      # If I type something other than a number
                 print("Ivalid value, please check.")
    expense.append(expense_day)     # the dictionary with {"category" : expense} will be added to the expense list. Each dictionary is equivalent to one day
    

print("total expense") # Calculate total daily spending by adding all categories
total = 0
for i, day in enumerate(expense, 1): 
    total_day = 0       
    for expence in day.values():
        total_day += expence
        total += expence
    print(f"Day {i}: {day}.")
    print(f"Today you have spent: {total_day}€.\n")
    

modify_expenses = input("You want to change some expenses? (y/n): ")

while modify_expenses.lower() == "y":
     day = int(input("Insert the day to modify (es. 1, 2, 3...): ")) - 1
     category = input("Enter the category to edit: ").lower()

     if day >= 0 and day < len(expense) and category in expense[day]:
        new_expense = float(input(f"Enter the new expense for {category} of the day {day + 1}: "))
        expense[day][category] = new_expense
        print("Modify correctly.")

        total = 0
        for i, day in enumerate(expense, 1): 
            total_day = 0       
            for expenses in day.values():
                total_day += expenses
                total += expenses
            print(f"Day {i}: {day}.")
            print(f"Today you have spent: {total_day}€.\n")
            
     else:
        print("Day or category wrong, try again")
     modify_expenses = input("Do you want to change other values? (y/n): ")



# sum of every expenses of all category
total_categories = {category: 0 for category in categories} # I create a dictionary where each key is a category and each value is the total expenses of that category
total_general = 0

for day in expense:
    for category in categories:
        total_categories[category] += day[category]

print("\n--- TOTAL EXPENSE CATEGORIES ---")        
for category, total in total_categories.items():      
    print(f"- {category}: {total}€")

         
print(f"\nYou spent a total of: {total:.2f}€")

remainder = budget_amount - total
if remainder > 0:
     print(f"Available budget: {remainder:.2f}€\n")
elif remainder == 0:
     print("You've used up your entire budget for this trip\n")
else:  
     print(f"You went over budget for {abs(remainder):.2f}€\n")


print("*" * 60)
print("     Thanks for using this Travel Expense Tracking App")
print("*" * 60)
