button_label = "submit"
print(button_label.capitalize())

password = input("What is your password? ")
attempts = 1

while password != "pass123" and attempts < 5:
    attempts += 1
    print(f'Incorrect Password and this is your {attempts} attempt. You have {5 - attempts} more to go!')
    password = input("What is your password?")
    
    
if password == "pass123":
    print(f'Password correct')
else:
    print("You failed")
