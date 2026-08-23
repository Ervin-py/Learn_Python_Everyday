#lists

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

    #apple
    #banana
    #cherry

#String

for x in "banana":
  print(x) 

    #b
    #a
    #n
    #a
    #n
    #a

#break statement(Stops the loop)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

    #apple
    #banana

#Exit the loop when x is "banana", but this time 
#the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

    #apple

#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

    #apple
    #cherry

#range() function
for x in range(6):
  print(x) 

    #0
    #1
    #2
    #3
    #4
    #5

#start and stop range
for x in range(2, 6):
  print(x)

    #2
    #3    
    #4
    #5

#increment by 3 (default is 1)
for x in range(2, 30, 3):
  print(x)

    #2
    #5
    #8
    #11
    #14
    #17
    #20
    #23
    #26
    #29

#Else in for loop
#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)  
else:
  print("Finally finished!")

    #0
    #1
    #2
    #3
    #4
    #5
    #Finally finished!


for x in range(6):
    if x == 3: 
        break
    print(x)
else:
    print("Finally finished!")

    #1. for x in range(6):
    #This means x will take values from 0 to 5.

    #2. Iteration process
    #x = 0 → condition x == 3 is False → prints 0.

    #x = 1 → prints 1.

    #x = 2 → prints 2.

    #x = 3 → condition x == 3 is True → break stops the loop immediately.

    #3. The else block
    #In Python, a for loop can have an else clause.

    #The else runs only if the loop finishes normally (without hitting break).

    #Since the loop was stopped early at x == 3, the else block is skipped.

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)

    #red apple
    #red banana
    #red cherry
    #big apple
    #big banana
    #big cherry
    #tasty apple
    #tasty banana
    #tasty cherry

#pass
for x in [0, 1, 2]:
  pass

#1. for x in [0, 1, 2]:
#This means the loop will run three times, with x taking values 0, 1, and 2.

#2. pass
#The pass statement is a placeholder.

#It tells Python: “Do nothing here, but keep the code valid.”

#Without pass, if you leave the loop body empty, Python raises an IndentationError because it expects something inside the block.