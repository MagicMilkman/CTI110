#Philip Corey
#9/28/23
#input and output for budget

budget = int(input("enter budget: "))
dest = input("enter destination: ")
gas  = int(input("enter how much you'll spend on gas: "))
accommodation  = int(input("enter how much you'll spend on accommodation: "))
food  = int(input("how much you'll spend on food: "))

netExpense = budget + gas + accommodation + food 
print("overall expenses: ", netExpense)
print("budget - net expenses = ", budget - netExpense)
