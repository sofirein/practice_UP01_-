import json 
students = [
    {"nave":"Анна","score":75},
    {"name":"Иван","score":45},
    {"name":"Олег","score":90}
]
for student in students:
    if student["score"] >= 60:
        student["result"] = "Зачёт"
    else:
        student["result"] = "Незачёт"

for student in students:
    print(student["name"], student["result"])

with open("students.json","w", encoding="utf-8") as file:
    json.dump(students,file,ensure_ascii=False)