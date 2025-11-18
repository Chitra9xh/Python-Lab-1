grades={"Pavan":90,"Aditi":85,"Rohan":88}
name=input("Enter a student's name: ")
try:
    print("Grade:",grades[name])
except KeyError:
    print("Error: Student",name,"not found.")
