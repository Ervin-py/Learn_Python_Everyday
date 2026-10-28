#On weekeends do Git

#drawing = {
#    "DWG-001":"Pump Assembly"
#}
#key - DWG-001
#list - ["Pump Assembly", "A", "Released"]

#drawing = {
#    "DWG-001": ["Pump Assembly", "A", "Released"]
#}

#print("DWG-001")
#for item in drawing["DWG-001"]:
#item - assign variable
#see drawing one by one
#    print(item)

drawing = [
{
    "drawing_number": "DWG-001",
    "name": "Pump Assembly",
    "revision": "A",
    "status": "Released"
},
{
    "drawing_number": "DWG-002",
    "name": "Shaft Assembly",
    "revision": "B",
    "status": "WIP"
},
{
    "drawing_number": "DWG-003",
    "name": "Gear Assembly",
    "revision": "C",
    "status": "Released"
}
]

for item in drawing:
    for key, value in item.items():
        print(f"{key}: {value}")