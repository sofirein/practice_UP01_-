students = {
    {"name": "Анна", "score": 75},
    {"name": "Иван", "score": 45},
    {"name": "Олег", "score": 90}
}

for student in students:
    if student["score"] >= 60:
        print(student["name"], "— Зачёт")
    else:
        print(student["name"], "— Незачёт")