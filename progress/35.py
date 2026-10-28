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
    while True:
        search = input("Enter Drawing number you want to search: ").upper()             

        if not validate_dwg(search):
            return

        if search_dwg(drawing, search):
            print_info(search_dwg(drawing, search))

        else:
            print("Drawing not found")

        if should_exit():
            break

def add_drawing():
    while True:
        #user input
        search = input("Enter a new drawing number: ").upper()

        if not validate_dwg(search):
            return

        #if state has values
        if search_dwg(drawing, search):
            print("Drawing already exists")
            return
            
        else:
            name = input("Enter a new name: ")
            revision = input("Enter a new revision: ").upper().strip()

            if not validate_revision(revision):
                return

            status = input("Enter a new status: ").upper().strip()

            if validate_status(status):

                create_dwg = create_drawing(search, name, revision, status)
                drawing.append(create_dwg)
                print("Drawing Was Added Succesfully") 

            else:
                print("Invalid format")
                print("Input: RELEASED/WIP/OBSOLETE")

        if should_exit():
            break

def create_drawing(search, name, revision, status):
    create_dwg = {        
        "drawing_number": search,
        "name": name,
        "revision": revision,
        "status": status
    }
    return create_dwg

def update_drawing():
    while True:
        list_dwg(drawing) 
        search = input("Enter the Drawing number you want to update: ").upper()

        if not validate_dwg(search):
            return

        if search_dwg(drawing, search):
            print_info(search_dwg(drawing, search))
            while True:                          
                    print("1. Drawing name")
                    print("2. Status")                           
                    print("3. Revision")
                    print("4. Exit")
                    try:
                        updates = input("Enter the number: ")  
                        update = int(updates.strip())       
                                            
                        if update == 1:
                            update_name = input("Enter new name: ")
                            search_dwg(drawing, search)["name"] = update_name
                            print("Drawing updated successfully")
                            
                        elif update == 2:
                            status = input("Enter new status: ").upper().strip() 
            
                            if validate_status(status):
                                search_dwg(drawing, search)["status"] = status
                                print("Drawing updated successfully")
                                
                            else:
                                print("Invalid format")
                                print("Input: RELEASED/WIP/OBSOLETE")
                                return                            
                            
                        elif update == 3:
                            update_revision = input("Enter new revision: ").upper().strip()

                            if not validate_revision(update_revision):
                                return

                            search_dwg(drawing, search)["revision"] = update_revision
                            print("Drawing updated successfully")
                            
                        elif update == 4:
                            break
            
                        else:
                            print("Please choose from 1-4 only")
                            
                    except ValueError:
                        print("Invalid format")

        
        else:
            print("Drawing not found")
        if should_exit():
            break   

def delete_drawing():
    while True:
        list_dwg(drawing)
        search = input("Enter Drawing Number you want to delete: ").upper()

        if not validate_dwg(search):
            return

        if search_dwg(drawing, search):
            drawing.remove(search_dwg(drawing, search))
            print("Drawing deleted successfully")
            return

        else:
            print("Drawing not found")  

        if should_exit():
            break     

def filter_drawing(drawing):
    while True:    
        print("Input: ")
        print("RELEASED")
        print("WIP")
        print("OBSOLETE")
        search = input("Enter status of drawing you want to filter: ").upper().strip()

        if validate_status(search):
            results = []
            for item in drawing:
                if item["status"].upper().strip() == search:
                    results.append(item)
            list_dwg(results)

        else:
            print("Invalid format")
            print("Input: RELEASED/WIP/OBSOLETE")
        if should_exit():
            break

def validate_revision(revision):
    if revision.isalpha() and len(revision) == 1:
        return True

    elif revision.isalpha() and len(revision) != 1:
        print("Invalid format")
        print("One character only")
        print("Ex: A, B, C")
        return False

    elif revision.isdigit():
        print("Invalid format")
        print("letters only")
        print("Input: A-Z/a-z only")
        return False

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
        return True

    else: 
        return False

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

def list_drawing():
    while True:
        list_dwg(drawing)
        if should_exit():
            break 

def list_dwg(drawing):

    for item in drawing:
        dwgno = item["drawing_number"]
        dwgname =  item["name"]
        rev =  item["revision"]
        stats =  item["status"]
        print(f"{dwgno} | {dwgname} | {rev} | {stats}")    


while True:
    
    print("1. Search Drawing\n2. Add Drawing\n3. Update Drawing\n4. Delete Drawing")

    print("5. List all drawings")
    print("6. Filter by status")
    
    try:
        chooses = input("Enter number you want to do: ")
        choose = int(chooses.strip())

        if choose == 1:

            search_drawing()
                #if True then break (True = Yes)
                
        #ADD
        elif choose == 2:

            add_drawing()
        
        #UPDATE
        elif choose == 3:

            update_drawing()


        elif choose == 4:

            delete_drawing()

  
                    
        elif choose == 5:

            list_drawing()

                               
        
        elif choose == 6:
            filter_drawing(drawing)
         

        else:
            print("Please choose from 1-6 only")

    except ValueError:
        print("Invalid format")



