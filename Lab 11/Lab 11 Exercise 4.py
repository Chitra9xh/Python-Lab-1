lst=[10,20,30,40,50]
try:
    idx=int(input("Enter index: "))
    print("Item:",lst[idx])
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Input must be a number.")
else:
    print("Successfully retrieved item.")
finally:
    print("--- List access attempt complete ---")
