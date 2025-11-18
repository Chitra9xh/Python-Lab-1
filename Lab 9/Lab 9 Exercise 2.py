def greet_user(username,greeting="Welcome"):
    return f"{greeting}, {username}!"

print(greet_user(input("Enter username: ")))
print(greet_user(input("Enter username: "),input("Enter custom greeting: ")))
