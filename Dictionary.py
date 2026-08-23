#dictionary
dictionary = {		
    'key1' : 'value1',		
    'key2': 'value2'		
}		

#List of dictionaries

drawing = [
    {
        "drawing_number": "DWG-001",
        "name": "Shaft Assembly",
        "revision": "A",
        "status": "Released"
    },
    {
        "drawing_number": "DWG-002",
        "name": "Gear Assembly",
        "revision": "B",
        "status": "WIP",
    },
    {
        "drawing_number": "DWG-003",
        "name": "Motor Assembly",
        "revision": "C",
        "status": "Released"
    }
]



#Operations
pizza = {				
    'name': 'Margherita Pizza',				
    'price': 8.9,				
    'calories_per_slice': 250				
}	

    #print the number of items
print(len(pizza))
    #3



    #Variable assignment

fields = [("name", "Margherita Pizza"), ("price", 8.9)]
pizza = dict(fields)

    
x = pizza["name"]
print(x)
    #Margharita Pizza
x = pizza.get("name")
print(x)
    #Margharita Pizza same as above

x = pizza.keys()
print(x)				
    # dict_keys(['name', 'price', 'calories_per_slice'])				
				
x = pizza.values()	
print(x)			
    # dict_values(['Margherita Pizza', 8.9, 250])				
				
x = pizza.items()	
print(x)			
    # dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])				



    #Accessing dictionary values
pizza = {				
    'name': 'Margherita Pizza',				
    'price': 8.9,				
    'calories_per_slice': 250				
}							

pizza["name"] = "try"
print(pizza)
    # {
    #  'name': 'try',
    #  'price': 8.9,
    #  'calories_per_slice': 250,

pizza["name_2"] = "Pepperoni Pizza"
print(pizza)
    # {
    #  'name': 'Margherita Pizza',
    #  'price': 8.9,
    #  'calories_per_slice': 250,
    #  'name_2': 'Pepperoni Pizza'  
    # }

pizza.update({"name_2", "Pepperoni Pizza"})
print(pizza)
    # {
    #  'name': 'Margherita Pizza',
    #  'price': 8.9,
    #  'calories_per_slice': 250,
    #  'name_2': 'Pepperoni Pizza'  
    # }

#if none in the orig dictionary it will be added
#if there it will be overwritten



    #deletes specific key name
pizza.pop("price")
print(pizza)
    # {
    #   'name': 'Margherita Pizza',
    #   'calories_per_slice': 250 
    # }

    #deletes last added item
pizza.popitem()
print(pizza)
    # {
    #   'name': 'Margherita Pizza', 
    #   'price': 8.9
    # }

    #deletes specific key name
del pizza["calories_per_slice"]
print(pizza)
    # {
    #   'name': 'Margherita Pizza', 
    #   'price': 8.9
    # }

    #empties the dictionary
pizza.clear()
print(pizza)
    #{}


    #copy the dictionary and assign it to a new variable
mydict = pizza.copy()
#or
mydict = dict(pizza)
print(mydict)




#Looping through a dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

    #or
for x in thisdict.keys():
  print(x)

    #brand
    #model
    #year

for x in thisdict:
  print(thisdict[x])

    #Ford
    #Mustang
    #1964

for x, y in thisdict.items():
  print(x, y)

    #brand Ford
    #model Mustang
    #year 1964