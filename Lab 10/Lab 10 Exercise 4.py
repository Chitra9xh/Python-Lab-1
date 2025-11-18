def check_length(password): return len(password)>8
def check_uppercase(password): return any(c.isupper() for c in password)
def check_number(password): return any(c.isdigit() for c in password)

validation_checks=[check_length,check_uppercase,check_number]
my_pass= input("Enter Password: ")
for check in validation_checks: print(check.__name__,":",check(my_pass))
