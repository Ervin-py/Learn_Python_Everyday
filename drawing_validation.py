
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

    else:
        print("Invalid format")
        print("Ex: A, B, C")
        print("Input: A-Z/a-z only")
        return False

def validate_status(status):

    if status in ["RELEASED", "WIP", "OBSOLETE"]:
        return True

    else: 
        return False
