def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

ops={"add":add,"sub":sub,"mul":mul,"div":div}
o=input("Enter operation (add/sub/mul/div): ")
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print("Result:",ops[o](a,b))
