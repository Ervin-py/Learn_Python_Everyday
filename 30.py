drawing = [
    {
        "drawing_number": "DWG-001",
        "name": "Shaft Assembly",
        "revision": "A",
        "status": "RELEASED"
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
        "status": "OBSOLETE"
    }
]

def search_drawing():
   
    search = input("Enter Drawing number you want to search: ").upper()             

    valid = validate_dwg(search)

    if not valid:
        return

    state = search_dwg(drawing, search)
    
    if state:
        print_info(state)

    else:
        print("Drawing not found")

def add_drawing():

    #user input
    search = input("Enter a new drawing number: ").upper()

    #validate
    valid = validate_dwg(search)

    if not valid:
        return

    #search drawing
    state = search_dwg(drawing, search)                

    #if state has values
    if state:
        print("Drawing already exists")
        
    else:
        name = input("Enter a new name: ")
        revision = input("Enter a new revision: ").upper().strip()
        valid_revision = validate_revision(revision)

        if not valid_revision:
            return

        else:
            status = input("Enter a new status: ").upper().strip()
            status = validate_status(status)

            if status:

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
                print("Input: RELEASED/WIP/OBSOLETE")

def update_drawing():
        list_dwg(drawing) 
        search = input("Enter the Drawing number you want to update: ").upper()

        valid = validate_dwg(search)

        if not valid:
            return

        state = search_dwg(drawing, search)

        if state:
            print_info(state)
            while True:
                    print("1. Drawing number")                            
                    print("2. Drawing name")
                    print("3. Status")                            
                    print("4. Revision")
                    print("5. Exit")
                    try:
                        updates = input("Enter the number: ")  
                        update = int(updates.strip())
                        
                        if update == 1:
                            search_2 = input("Enter new number: ").upper()                                        
            
                            valid_2 = validate_dwg(search_2)
            
                            if not valid_2:
                                continue
            
                            state_2 = search_dwg(drawing, search_2)

                            if not state_2:
                                search_2 = search_2.upper()                                                       
                                state["drawing_number"] = search_2
                                print("Drawing updated successfully")
            
                            elif search == search_2:
                                print("Same drawing number entered")
            
                            elif state_2:
                                print("Drawing number already exist")                                  
                                            
                        elif update == 2:
                            update_name = input("Enter new name: ")
                            state["name"] = update_name
                            print("Drawing updated successfully")
                            
                        elif update == 3:
                            status = input("Enter new status: ").upper().strip() 
            
                            status = validate_status(status) 
            
                            if status:
                                state["status"] = status
                                print("Drawing updated successfully")
                                
                            else:
                                print("Invalid format")
                                print("Input: RELEASED/WIP/OBSOLETE")
                                continue                            
                            
                        elif update == 4:
                            update_revision = input("Enter new revision: ").upper().strip()
            
                            if update_revision.isalpha() and len(update_revision) != 1 and len(update_revision) != 0:
                                print("Invalid format")
            
                            else:
                                state["revision"] = update_revision
                                print("Drawing updated successfully")
                            
                        elif update == 5:
                            break
            
                        else:
                            print("Please choose from 1-5 only")
                            
                    except ValueError:
                        print("Invalid format")

        
        else:
            print("Drawing not found")   

def delete_drawing():
    while True:
        if should_exit():
            break

        search = input("Enter Drawing Number you want to delete: ").upper()

        valid = validate_dwg(search)

        if not valid:
            continue

        state = search_dwg(drawing, search)

        if state:
            drawing.remove(state)
            print("Drawing deleted succesful")
            break

        else:
            print("Drawing not found")

def list_drawing():
    while True:
        list_dwg(drawing) 
        if should_exit():
            break

def filter_drawing():
    #FILTER
        while True:
            if should_exit():
                break
    
            print("Input: ")
            print("RELEASED")
            print("WIP")
            print("OBSOLETE")
            search = input("Enter status of drawing you want to filter: ").upper()

            matched = status_filter(drawing, search)

            if matched:
                list_dwg(matched)

            else:
                print("Drawing does not exist")

def validate_revision(revision):
    if revision.isalpha() and len(revision) != 1 and len(revision) != 0:
        print("Invalid format")
        print("Input: A-Z, A1-Z1, A2-Z2, etc.")
        return False
    
    else:
        return True


#def_exit
def should_exit():
    while True:
        user_input = input("Exit? y/n: ").lower().strip()
        if user_input == "y":
            return True                    

        elif user_input == "n":
            return False
            #False skips the break part

        else:
            print("Invalid format")

def validate_status(status):

    if status in ["RELEASED", "WIP", "OBSOLETE"]:
        return status

def validate_dwg(search):

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

    return True

def search_dwg(drawing, search):

    for state in drawing:
        if state["drawing_number"] == search:
            return state
    
    #Indentation here if you want to check all the list of dict first
    return None                    

def print_info(state):
    for key, value in state.items():
        print(f"{key} : {value}")

def status_filter(drawing, search):
    results = []
    for item in drawing:
        if item["status"].upper().strip() == search:
            results.append(item)
    return results

def list_dwg(drawing):
    for item in drawing:

        dwgno = item["drawing_number"]
        dwgname =  item["name"]
        rev =  item["revision"]
        stats =  item["status"]
        print(f"{dwgno} | {dwgname} | {rev} | {stats}")    

while True:
    
    print("1. Search drawing")
    print("5. List all drawings")
    print("6. Filter by status")
    
    try:
        chooses = input("Enter number you want to do: ")
        choose = int(chooses.strip())

        if choose == 1:
            while True:
                search_drawing()
                #if True then break (True = Yes)
                if should_exit():
                    break
        #ADD
        elif choose == 2:
            while True:
                add_drawing()

                if should_exit():
                    break          
        #UPDATE
        elif choose == 3:
            while True:
                update_drawing()

                if should_exit():
                    break

        elif choose == 4:
            delete_drawing()
                    
        elif choose == 5:
            list_drawing()
                                    
        
        elif choose == 6:
            filter_drawing()               

        else:
            print("Please choose from 1-6 only")

    except ValueError:
        print("Invalid format")



