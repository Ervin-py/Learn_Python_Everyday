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

while True:
    drawing_no = input(f"Enter drawing_number: ")
    found = False
    
    for item_drawing in drawing:       
        if drawing_no == item_drawing["drawing_number"]:
            found = True
            for key, value in item_drawing.items():
                print(f"{key}: {value}")
                print("Update value?")
                print("1. drawing_number")
                print("2. name")
                print("3. revision")
                print("4. status")
                print("5. exit")
                update_item = input(f"Enter number you want to update: ")
                if update_item == "1":
                    new_drawing_number = input("Enter new drawing no: ")
                    item_drawing["drawing_number"] = new_drawing_number
                elif update_item == "2":
                    new_name = input("Enter new name: ")
                    item_drawing["name"] = new_name         
                elif update_item == "3":
                    new_revision = input("Enter new revision: ")
                    item_drawing["revision"] = new_revision     
                elif update_item == "4":
                    new_status = input("Enter new status: ")
                    item_drawing["status"] = new_status     
                elif update_item == "5":
                    break
                else:
                    print("Invalid input")

if found is False:
    print("Item not found")