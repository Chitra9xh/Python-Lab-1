student_db={101:"Aarav",105:"Priya",110:"Rahul",124:"Sonia"}
roll=int(input("Enter roll number: "))
print("Result:",student_db.get(roll,"Student not found"))
