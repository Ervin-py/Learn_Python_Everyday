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

    
    print("1. Search drawing\n2. Add drawing\n3. Update drawing\n4. Delete drawing")
    print("5. List all drawings")
    print("6. Filter by status")

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

    elif choose == "2":
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
                
                #should be 7 charactes of length
                if len(search) != 7:
                    found = True
                    print("Invalid format must be 7 characters: DWG-XXX")
                    print("Ex: DWG-123")
                  
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
                    
                elif not found:
                    name = input("Enter name: ")
                    revision = input("Enter revision: ")
                    status = input("Enter status: ")
                    adddrawing = {        
                                    "drawing_number": search,
                                    "name": name,
                                    "revision": revision,
                                    "status": status
                                }
                    drawing.append(adddrawing)
                    print("Drawing Was Added Succesfully") 
            else:
                print("Invalid input")                  

    elif choose == "3":
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
                        print("Current State: ")
                        for key, value in state.items():
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
                            
                            for item in drawing:                
                                if item["drawing_number"] == update_number:
                                    exists = True
                                    break
                            
                            if exists:
                                print("Drawing number already exists")

                                                    
                            else:
                                state["drawing_number"] = update_number
                                print("Drawing updated successfully")
                                            
                        elif update == "2":
                            update_name = input("Enter new name: ")
                            state["name"] = update_name
                            print("Drawing updated successfully")
                            
                        elif update == "3":
                            update_status = input("Enter new status: ")
                            state["status"] = update_status
                            print("Drawing updated successfully")
                            
                        elif update == "4":
                            update_revision = input("Enter new revision: ")
                            state["revision"] = update_revision
                            print("Drawing updated successfully")
                            
                        elif update == "5":
                            break
                                    
                if not found:
                    print("Drawing not found") 

            else:
                print("Invalid input")

    elif choose == "4":
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
                        drawing.remove(state_4)
                        print("Drawing deleted succesful")
                        break

                if not found:
                    print("Drawing not found")
            else:
                print("Invalid input") 
                
    elif choose == "5":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break

            elif user_input == "n":
                for item in drawing:
                    dwgno = item["drawing_number"]
                    dwgname =  item["name"]
                    rev =  item["revision"]
                    stats =  item["status"]
                    print(f"{dwgno} | {dwgname} | {rev} | {stats}")  
                
                
                
            else:
                print("Invalid input") 

    elif choose == "6":
        while True:
            user_input = input("Exit? y/n: ")
            if user_input == "y":
                break
            
            elif user_input == "n":
    
                print("Input: ")
                print("Released")
                print("WIP")
                print("Obsolete")
                user = input("Enter status of drawing you want to filter: ")
                
                cap = user.upper()
                found = False
                
                #Show all Released
                
                if cap == "RELEASED":
                    for item in drawing:
                        if item["status"] == "WIP" or item["status"] == "Obsolete": #skips WIP
                            continue
                        dwgno = item["drawing_number"]
                        dwgname =  item["name"]
                        rev =  item["revision"]
                        stats =  item["status"]
                        print(f"{dwgno} | {dwgname} | {rev} | {stats}")  

                    if not found:
                        print("No drawings found with that status.")
                        found = True

                
                elif cap == "WIP":
                    for item in drawing:
                        if item["status"] == "Released" or item["status"] == "Obsolete": 
                            continue
                        dwgno = item["drawing_number"]
                        dwgname =  item["name"]
                        rev =  item["revision"]
                        stats =  item["status"]
                        print(f"{dwgno} | {dwgname} | {rev} | {stats}") 
                        found = True

                    if not found:
                        print("No drawings found with that status.")
                        
                        
                        
                elif cap == "OBSOLETE":
                    for item in drawing:
                        if item["status"] == "WIP" or item["status"] == "Released": 
                            continue
                        dwgno = item["drawing_number"]
                        dwgname =  item["name"]
                        rev =  item["revision"]
                        stats =  item["status"]
                        print(f"{dwgno} | {dwgname} | {rev} | {stats}")
                        found = True
                        
                    if not found:
                        print("No drawings found with that status.")
                else:
                    print("Invalid format")

  
                    
                
                
            else:
                print("Invalid input") 

                
    else:
        print("Invalid Input")


