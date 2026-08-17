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
    print("3. Add drawing")
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


                if found == False:
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

                if found == False:  
                    name = input("Enter name: ")
                    revision = input("Enter revision: ")
                    status = input("Enter status: ")
                    drawing.append({        
                        "drawing_number": search,
                        "name": name,
                        "revision": revision,
                        "status": status
                    })

            else:
                print("Invalid input")                  

    if choose == "3":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break

            elif user_input == "n":
                search = input("Enter drawing_number you want to update: ")
                found = False

                for state in drawing:
                    if state["drawing_number"] == search:  
                        found = True
                        for key, value in state.items():
                            print(f"{key} : {value}")
                            print("Enter number you want to update")
                            print("1. Drawing number")                            
                            print("2. Drawing name")
                            print("3. Status")                            
                            print("4. Revision")
                            update = input("Enter here: ")                            
                            if update == "1":
                                update_number = input("Enter new number: ")
                                state["drawing_number"] = update_number
                                print(drawing)
                            if update == "2":
                                update_name = input("Enter new name: ")
                                state["name"] = update_name
                                print(drawing)
                            if update == "3":
                                update_status = input("Enter new status: ")
                                state["status"] = update_status
                                print(drawing)
                            if update == "4":
                                update_nrevision = input("Enter new revision: ")
                                state["drawing_number"] = update_revision
                                print(drawing)

                if found == False:
                    print("Drawing not found") 

            else:
                print("Invalid input")
  


