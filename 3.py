#drawing_number: DWG-003
#name: Gear Assembly
#revision: C
#status: Released

#check yt for true or False

drawing = [
    {
        "drawing_number" : "DWG-001",
        "name" : "Shaft Assembly",
        "revision" : "A",
        "status" : "Released"
    },
    {
        "drawing_number" : "DWG-002",
        "name" : "Gear Assembly",
        "revision" : "B",
        "status" : "WIP",
    },
    {
        "drawing_number" : "DWG-003",
        "name" : "Motor Assembly",
        "revision" : "C",
        "status" : "Released"
    }
]


store = input(f"Enter drawing_number: ")
Error = False

for item in drawing:
    
        if store == item["drawing_number"]:
            print(f"Drawing found!")
            print(f"Current information:") 
            for key, value in item.items():
                print(f"{key} : {value}")
            print(f"What do you want to update?")
            print(f"1. Revision")  
            print(f"2. Status")    
            print(f"3. Cancel")                                                              
            new_revision = input(f" Enter new revision: ")
            if new_revision:
                item["revision"] = new_revision 
                print("updated")

            new_status = input(f" Enter new status: ")
            if new_status:
                item["status"] = new_status 
                print("updated")
            Error = True


if Error is False:
    print("Item not found")


#for items in drawing:
#    for key, value in items.items():
#        print(f"{key} : {value}")

