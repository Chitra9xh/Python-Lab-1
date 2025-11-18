def set_pct(p):
    if p<0 or p>100: raise ValueError("Percentage must be between 0 and 100.")
    print("Setting percentage to",p,"%")

try:
    set_pct(int(input("Enter percentage: ")))
except ValueError as e:
    print("Error:",e)
