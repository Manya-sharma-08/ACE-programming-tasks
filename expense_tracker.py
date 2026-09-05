# Expense Tracker Project - easy task 1

expenses = [] #list of expenses

print("   Welcome to your expense tracker   ")

while True:
    print("------MENU------")
    print("1. Add Expense ")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")
    print("----------------")

    choice = int(input("Please, Enter your choice :"))

# to add the expense

    if choice == 1:
        date = input("Enter the date :")
        amount = int(input("Enter the amount spend : $"))
        category = input("Enter the category of purchase (eg. food, travel, etc) :")
        description = input("Enter a short description of your expense :")

        a = {
            "Date" : date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        expenses.append(a)
        print("\n Expense added successfully ")

# to view expenses
    elif choice == 2:
        if len(expenses) == 0 :
          print("No expenses added")
        else:
          print("----------------")
          print("    Expenses    ")
          print("----------------")

          total = 0
          count = 1
          for i in expenses:
             print(f"Expense Number {count} -> ${i["Amount"]},{i["Category"]}\n{i["Description"]}")
             count = count + 1
             total = total + int(i["Amount"])
             print("Total amount :",total)

# to view summary
                   
    elif choice == 3:
       print("----------------")
       print("    Summary     ")
       print("----------------")



       
       for i in expenses:
         print("----------------") 
         print(f"On {i["Date"]},an expense was made of amount : ${i["Amount"]}\n Description : {i["Description"]}")
         print
         print("----------------")
        
# to exit
       
    elif choice == 4:
       print("Exiting.........Goodbye!!\n Thank you")
       break

# in case of invaild input 

    else : 
       print("Invalid input,please try again")

# End of code          