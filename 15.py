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

        #def_exit
        def exit():
            while True:
                user_input = input("Exit? y/n: ").lower().strip()
                if user_input == "y":
                    return True                    
        
                elif user_input == "n":
                    return False
                    #False skips the break part

                else:
                    print("Invalid format")

        def search_dwg(drawing, search):
            for state in drawing:
                if state["drawing_number"] == search:
                    return state

            #Indentation here if you want to check all the list of dict first
            return None                 

        def print_info(state):
            for key, value in state.items():
                print(f"{key} : {value}")



        def validation(search):
            
        #should be 7 charactes of length
            if len(search) != 7:  
                print("Invalid format must be 7 characters: DWG-XXX")
                print("Ex: DWG-123")
                return False
                
            #alpha - first 3 digits should be A-z
            #upper - first 3 digits can be lower   
            elif not search[:3].isalpha() or search[:3].upper() != "DWG":
                print("Invalid format must start with: DWG")
                print("Ex: DWG-123")
                return False
                
            elif search[3] != "-":                      
                print("Invalid format missing dash after DWG")
                print("Ex: DWG-123")
                return False
            
            elif not search[4:].isdigit():                     
                print("Invalid format last 3 digits must be numbers")
                print("Ex: DWG-123")
                return False

            else:
                return True             
         
        if choose == 1:
            while True:    
                #if True then break (True = Yes)
                if exit():
                    break

                search = input("Enter drawing_number: ")
                if not validation(search):
                    continue

                state = search_dwg(drawing, search)              

                if state:
                    print_info(state)

                else:
                    print("Drawing not found")

        #ADD
        elif choose == 2:
            while True:
                if exit():
                    break
        
                search = input("Enter a new drawing number: ")
                if not validation(search):
                    continue

                state = search_dwg(drawing, search)                

                #if state has values
                if state:
                    print("Drawing already exists")
                    
                else:
                    name = input("Enter a new name: ")
                    revision = input("Enter a new revision: ")
                    statuss = input("Enter a new status: ")
                    valid = False
                    status = statuss.upper()
    
                    if status in ["RELEASED", "WIP", "OBSOLETE"]:
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

        #UPDATE
        elif choose == 3:
            while True:
                if exit():
                    break

                search = input("Enter the Drawing number you want to update: ")

                #if drawing is valid then continue(True)
                if not validation(search):
                    continue

                state = search_dwg(drawing, search)

                if state:
                    print_info(state)

                    print("1. Drawing number")                            
                    print("2. Drawing name")
                    print("3. Status")                            
                    print("4. Revision")
                    print("5. Exit")
                    try:
                        updates = input("Enter the number you want to update: ")  
                        update = int(updates.strip())
                        
                        if update == 1:
                            update_number = input("Enter new number: ")                                                

                            if not validation(search):
                                continue  

                            state = search_dwg(drawing, search)

                            if not state:                                                       
                                state["drawing_number"] = update_number
                                print("Drawing updated successfully")

                            else:
                                print("Drawing already exist")                                  
                                            
                        elif update == 2:
                            update_name = input("Enter new name: ")
                            state["name"] = update_name
                            print("Drawing updated successfully")
                            
                        elif update == 3:
                            update_status = input("Enter new status: ")

                            if update_status in ["RELEASED", "WIP", "OBSOLETE"]:
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
                                
                else:
                    print("Drawing not found") 
        
        elif choose == 4:
            while True:
                if exit():
                    break
        
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
                if exit():
                    break
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
                if exit():
                    break
        
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



