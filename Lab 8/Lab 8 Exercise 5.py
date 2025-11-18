assignments={"Aarav":"Python","Priya":"Java","Rahul":"Python","Sonia":"C++","Vikram":"Java"}
inverted={}
for student,lang in assignments.items():
    inverted.setdefault(lang,[]).append(student)
print("Inverted dictionary:",inverted)
