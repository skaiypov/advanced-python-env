# Working with JSON Files 
#
# 1. Create a students.json file containing:
#    - name
#    - age
#    - grades (list)
#
# 2. Write a Python script that:
#    - Reads the JSON file
#    - Calculates the average grade per student
#    - Writes the updated data back to a new JSON file

import json

with open("students.json") as json_in:
    students = json.load(json_in)

    for i in students:
        grades = i["grades"]
        average = sum(grades) / len(grades)
        
        i["average_grade"] = int(average) #add new line

with open("students_upd.json", "w") as json_out:
    json.dump(students, json_out)    
