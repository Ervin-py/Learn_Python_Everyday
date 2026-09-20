drawing = [
    {"drawing_number": "001", "name": "Gear"},
    {"drawing_number": "002", "name": "Bolt"}
]

search = input("Enter drawing_number: ")

for state in drawing:
    if state["drawing_number"] == search:
        found = True
        for key, value in state.items():
            print(f"{key} : {value}")

#1
#for state in drawing:
#Loops through each element inside the variable drawing.
#→ First loop: state = {"drawing_number": "001", "name": "Gear"}  
#→ Second loop: state = {"drawing_number": "002", "name": "Bolt"}

#2
#if state["drawing_number"] == search:
#Checks if the "drawing_number" inside the current dictionary matches the variable search.
#If it matches, the code inside this if block will run.
#Example: If search = "002", only the second dictionary passes the condition.

#3
#found = True
#Marks that a matching drawing was found.
#This is useful if you want to later check whether the search succeeded or not.

#4
#for key, value in state.items():
#Loops through all key–value pairs inside the dictionary state.
#.items() returns something like [("drawing_number","002"), ("name","Bolt")].
#So key will be "drawing_number", then "name", and value will be "002", then "Bolt".

#5 
# print(f"{key} : {value}")
#Prints each key and its corresponding value in a nice format.
#Example output for the dictionary {"drawing_number": "002", "name": "Bolt"}:

#Code
#drawing_number : 002
#name : Bolt


found = False
if not found
#same as
if found is False


 #alpha - first 3 digits should be A-z
                #upper - first 3 digits can be lower   
                elif not search[:3].alpha() or search[:3].upper() != "DWG":
                    print("Invalid format must start with: DWG")
                    print("Ex: DWG-123")
                    
                elif search[3] != "-":
                    print("Invalid format missing dash after DWG")
                    print("Ex: DWG-123")
                
                elif not search[4:].isdigits():
                    print("Invalid format last 3 digits must be numbers")
                    print("Ex: DWG-123")


    #.strip() removes spaces around the input (so " 1" becomes "1").

    #int() converts the string to an integer, ignoring leading zeros (so "01" becomes 1).
    user = input("Enter a number: ")
    user = int(user.strip())


try:
    number = int(user_input.strip())
    print("You entered the number:", number)
except ValueError:
    print("That wasn’t a valid whole number.")

######
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
    #Functions can send data back to the code that called them using the return statement.

    #When a function reaches a return statement, it stops executing and sends the result back:

def x():
    While True

        if
            return True



    if X() means if x is True



##


if status in ["RELEASED", "WIP", "OBSOLETE"]

#is same below

if "RELEASED" == status or "WIP" == status or "OBSOLETE" == status:

###
