def gm(n): return f"Good morning, {n}!"
def ge(n): return f"Good evening, {n}!"

h=int(input("Enter hour (0-23): "))
f=gm if h<12 else ge
print(f(input("Enter name: ")))
