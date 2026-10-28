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
    
    try:
        chooses = input("Enter number you want to do: ")
        choose = int(chooses.strip())
        
        if choose == 1:
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
        
        elif choose == 2:
            while True:
                user_input = input("Exit? y/n: ")
                if user_input == "y":
                    break
        
                elif user_input == "n":
                    search = input("Enter drawing_number: ")
                    found = False
                    valid = True
                    for state in drawing:
                        if state["drawing_number"] == search:
                            found = True
                            print("Drawing already exists")
                    
                    #should be 7 charactes of length
                    if len(search) != 7:
                        valid = False
                        print("Invalid format must be 7 characters: DWG-XXX")
                        print("Ex: DWG-123")
                      
                    #alpha - first 3 digits should be A-z
                    #upper - first 3 digits can be lower   
                    elif not search[:3].isalpha() or search[:3].upper() != "DWG":
                        valid = False
                        print("Invalid format must start with: DWG")
                        print("Ex: DWG-123")
                        
                    elif search[3] != "-":
                        valid = False                       
                        print("Invalid format missing dash after DWG")
                        print("Ex: DWG-123")
                    
                    elif not search[4:].isdigit():
                        valid = False                       
                        print("Invalid format last 3 digits must be numbers")
                        print("Ex: DWG-123")
                        
                    elif valid and not found:
                        name = input("Enter name: ")
                        revision = input("Enter revision: ")
                        statuss = input("Enter status: ")
                        valid = False
                        status = statuss.upper()
        
                        if "Released" == status or "WIP" == status or "Obsolete" == status:
                            adddrawing = {        
                                    "drawing_number": search,
                                    "name": name,
                                    "revision": revision,
                                    "status": status
                                }
                            drawing.append(adddrawing)
                            print("Drawing Was Added Succesfully") 


                        else:
                            print("Invalid format")
                            continue               

                else:
                    print("Invalid input")                  
        
        elif choose == 3:
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
                            try:
                                updates = input("Enter here: ")  
                                update = int(updates.strip())
                                
                                if update == 1:
                                    update_number = input("Enter new number: ")
                                    exists = True
                                    value = True
                                    
                                    for item in drawing:                
                                        if item["drawing_number"] == update_number:
                                            exists = False
                                            break
            
                                    #should be 7 charactes of length
                                    if len(update_number) != 7:
                                        valid = False
                                        print("Invalid format must be 7 characters: DWG-XXX")
                                        print("Ex: DWG-123")
                                    
                                    #alpha - first 3 digits should be A-z
                                    #upper - first 3 digits can be lower   
                                    elif not update_number[:3].isalpha() or update_number[:3].upper() != "DWG":
                                        valid = False                                        
                                        print("Invalid format must start with: DWG")
                                        print("Ex: DWG-123")
                                        
                                    elif update_number[3] != "-":
                                        valid = False                                      
                                        print("Invalid format missing dash after DWG")
                                        print("Ex: DWG-123")
                                    
                                    elif not update_number[4:].isdigit():
                                        valid = False                                      
                                        print("Invalid format last 3 digits must be numbers")
                                        print("Ex: DWG-123")
                                    
                                    elif exists and valid:
                                        print("Drawing number already exists")
                                                            
                                    else:
                                        state["drawing_number"] = update_number
                                        print("Drawing updated successfully")
                                                    
                                elif update == 2:
                                    update_name = input("Enter new name: ")
                                    state["name"] = update_name
                                    print("Drawing updated successfully")
                                    
                                elif update == 3:
                                    update_status = input("Enter new status: ")

                                    if "Released" == status or "WIP" == status or "Obsolete" == status:
                                        state["status"] = update_status
                                        print("Drawing updated successfully")
                                        
                                    else:
                                        print("Invalid format")
                                        continue   

   
                                    
                                    
                                elif update == 4:
                                    update_revision = input("Enter new revision: ")
                                    state["revision"] = update_revision
                                    print("Drawing updated successfully")
                                    
                                elif update == 5:
                                    break



                                    
                            except ValueError:
                                print("Invalid format")
                                        
                    if not found:
                        print("Drawing not found") 
        
                else:
                    print("Invalid input")
        
        elif choose == 4:
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
                    
        elif choose == 5:
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
        
        elif choose == 6:
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
                    found = False
        
                    cap = user.upper()
        
                    for item in drawing:
                        if item["status"].upper() == cap:
                            dwgno = item["drawing_number"]
                            dwgname =  item["name"]
                            rev =  item["revision"]
                            stats =  item["status"]
                            print(f"{dwgno} | {dwgname} | {rev} | {stats}")
                            found = True
                        
                    if not found:
                        print("Drawing does not exist")
        
        
                        
                    
                    
                else:
                    print("Invalid input") 


                    
    except ValueError:
        print("Invalid format")



