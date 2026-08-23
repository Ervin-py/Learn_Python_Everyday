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