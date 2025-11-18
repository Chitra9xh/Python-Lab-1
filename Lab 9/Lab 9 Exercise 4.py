def calculate_average_grade(*grades):
    if len(grades)==0: return 0.0
    return sum(grades)/len(grades)

print("Average:",calculate_average_grade(90,85,88))
print("Average:",calculate_average_grade(75,82,95,89,91))
print("Average:",calculate_average_grade())
