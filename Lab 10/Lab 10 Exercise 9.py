def make_greeter(greeting):
    def greeter(name): return f"{greeting}, {name}!"
    return greeter

greet_hello=make_greeter("Hello")
greet_namaste=make_greeter("Namaste")

print(greet_hello("Pavan"))
print(greet_namaste("Aditi"))
