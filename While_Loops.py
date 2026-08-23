#While

#Infinite Loop
while True:
    print("Still running...")
    #This will run forever until you stop the program manually (Ctrl+C).

#Loop with a break statement
while True:
    password = input("Enter password: ")
    if password == "secret123":
        print("Access granted!")
        break
    else:
        print("Try again.")
