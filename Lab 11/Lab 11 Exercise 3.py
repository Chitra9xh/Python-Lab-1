try:
    n=int(input("Enter numerator: "))
    d=int(input("Enter denominator: "))
    print("Result:",n/d)
except ValueError:
    print("Error: Both inputs must be valid numbers.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
