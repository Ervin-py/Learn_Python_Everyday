#new_revision = input(f" Enter new revision: ")
#if new_revision:
#    item["revision"] = new_revision 
#    print("updated")

#new_status = input(f" Enter new status: ")
#if new_status:
#    item["revision"] = new_status 
#    print("updated")

#plan - Git git hub
#recall new concepts

drawing = [
    {
        "drawing_number" : "DWG-001",
        "drawing_name" : "Shaft Assembly",
        "Revision" : "A",
        "State" :  "Released"
    },
        {
        "drawing_number" : "DWG-002",
        "drawing_name" : "Gear Assembly",
        "Revision" : "B",
        "State" :  "WIP"
    },
        {
        "drawing_number" : "DWG-003",
        "drawing_name" : "Pipe Assembly",
        "Revision" : "C",
        "State" :  "Released"
    }
]


for item in drawing:
    store = input(f"Enter drawing_number: ")
    if key == item["drawing_number"]:
        print(f"Drawing found!")
        print(f"Current information:") 
        for key, value in item.items():
            print(f"{key} : {value}")
        print(f"What do you want to update?")
        print(f"1. Revision")  
        print(f"2. State")    
        print(f"3. Cancel")                                                              
        new_revision = input(f" Enter new revision: ")
        if new_revision:
            item["Revision"] = new_revision 
            print("updated")

        new_status = input(f" Enter new status: ")
        if new_status:
            item["State"] = new_status 
            print("updated")


#for item in drawing:
#    print(item)
#{'drawing_number': 'DWG-001', 'drawing_name': 'Shaft Assembly', 'Revision': 'A', 'State': 'Released'}
#{'drawing_number': 'DWG-002', 'drawing_name': 'Gear Assembly', 'Revision': 'B', 'State': 'WIP'}
#{'drawing_number': 'DWG-003', 'drawing_name': 'Pipe Assembly', 'Revision': 'C', 'State': 'Released'}

#print(drawing[0])
#{'drawing_number': 'DWG-001', 'drawing_name': 'Shaft Assembly', 'Revision': 'A', 'State': 'Released'}