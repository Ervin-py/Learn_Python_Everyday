drawing = [
{    
    "drawing_number": "DWG-001",
    "name": "Pump Assembly",
    "revision": "A",
    "status": "Released"
},
{  
    "drawing_number": "DWG-002",
    "name": "Shaft Assembly",
    "revision": "B",
    "status": "WIP"
},
{  
    "drawing_number": "DWG-003",
    "name" : "Gear Assembly",
    "revision" : "C",
    "status" : "Released"
}
]

#for item in drawing:
#    for key, value in item.items():
#        print(f"{key} : {value}")

#print(item.items())

store = input("Enter a value: ")
check = False
for item in drawing:
    if store == item["drawing_number"]:
        print(item)
if not check:
    print("Item not found")
#else 
#    return "Item not found"
#loop back to input
    