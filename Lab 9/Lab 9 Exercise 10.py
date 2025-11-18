def enroll_student(student_id,course_name,**options):
    print("Student ID:",student_id)
    print("Course:",course_name)
    if options.get("hostel"): print("Hostel accommodation requested:",options["hostel"])
    if options.get("scholarship"): print("Scholarship application submitted.")

enroll_student("S001","B.Tech CSE")
enroll_student("S002","B.Tech ECE",hostel="A-Block")
enroll_student("S003","B.Tech ME",scholarship=True,hostel="B-Block")
