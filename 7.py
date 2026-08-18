# Online Python compiler (interpreter) to run Python online.
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

while True:
    print("1. Search drawing")
    print("2. Add drawing")
    print("3. Update drawing")
    print("4. Update drawing")
    choose = input("Enter number you want to do: ")

    if choose == "1":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break

            elif user_input == "n":
                search = input("Enter drawing_number: ")
                found = False

                for state in drawing:
                    if state["drawing_number"] == search:
                        found = True
                        for key, value in state.items():
                            print(f"{key} : {value}")


                if not found:
                    print("Drawing not found")
            else:
                print("Invalid input")

    if choose == "2":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break

            elif user_input == "n":
                search = input("Enter drawing_number: ")
                found = False

                for state in drawing:
                    if state["drawing_number"] == search:
                        found = True
                        print("Drawing already exists")

                if not found:
                    name = input("Enter name: ")
                    revision = input("Enter revision: ")
                    status = input("Enter status: ")
                    drawing.append({        
                        "drawing_number": search,
                        "name": name,
                        "revision": revision,
                        "status": status
                    })
                    print("Added succesful") 
            else:
                print("Invalid input")                  

    if choose == "3":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break

            elif user_input == "n":
                search_2 = input("Enter drawing_number you want to update: ")
                found = False

                for state_2 in drawing:
                    if state_2["drawing_number"] == search_2:
                        found = True
                        for key, value in state_2.items():
                            print("Current state: ")
                            print(f"{key} : {value}")
                            print("1. Drawing number")                            
                            print("2. Drawing name")
                            print("3. Status")                            
                            print("4. Revision")
                            print("5. Exit")
                            update = input("Enter here: ")                            
                            if update == "1":
                                update_number = input("Enter new number: ")
                                exists = False
                                        
                                for item_2 in drawing:
                                    if item_2["drawing_number"] == update_number:
                                        exists = True
                                        print("Drawing is already named the same")
                                            
                                    else:
                                        item_2["drawing_number"] = update_number
                                        print(drawing)
                                            
                            elif update == "2":
                                update_name = input("Enter new name: ")
                                state_2["name"] = update_name
                                print(drawing)
                            
                            elif update == "3":
                                update_status = input("Enter new status: ")
                                state_2["status"] = update_status
                                print(drawing)
                            
                            elif update == "4":
                                update_revision = input("Enter new revision: ")
                                state_2["revision"] = update_revision
                                print(drawing)
                            
                            elif update == "5":
                                break
                                    
                if not found:
                    print("Drawing not found") 

            else:
                print("Invalid input")

    if choose == "4":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break

            elif user_input == "n":
                delete = input("Enter drawing_number you want to delete: ")
                found = False

                for state_4 in drawing:
                    if state_4["drawing_number"] == delete:
                        found = True
                        for key_4, value_4 in state_4.items():
                        del key_4,
                        del value_4
                        print(f"Deleted succesfully")


                if not found:
                    print("Drawing not found")
            else:
                print("Invalid input")  


