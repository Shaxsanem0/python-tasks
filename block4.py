#zadaniya s 16 po 20
#16
year=2024
if year%4==0:(
    print(f" this year is visocostniy")
)
else:(
        print(f"this year isnt visocostniy")
    )
#17
user_age=34
if user_age>0 and user_age<12:(
    print(f"this is children")
)
elif user_age>12 and user_age<18:(
    print(f"this is teenager")
)
elif user_age>18 and user_age<56:(
    print(f"this is adult")
)
else:(
print(f"this is pensioner")
    )
    #18
correct_username = "admin"
correct_password = "secretpassword"
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")
if entered_username == correct_username and entered_password == correct_password:
    print("Access granted! Welcome, admin.")
else:
    print("Access denied! Incorrect username or password.") 
    #19
month = int(input("Enter the month number (1-12): "))
if month == 12 or month == 1 or month == 2:
    print("This is Winter ")
    print("This is Spring ")
elif 6 <= month <= 8:
    print("This is Summer ")
elif 9 <= month <= 11:
    print("This is Autumn ")
else:
    print("Error: Invalid month number! Please enter a number from 1 to 12.")
#20
a = float(input("Enter the length of the first side (a): "))
b = float(input("Enter the length of the second side (b): "))
c = float(input("Enter the length of the third side (c): "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Success! A triangle with these sides can exist. ")
else:
    print("Error: A triangle with these sides CANNOT exist! ")