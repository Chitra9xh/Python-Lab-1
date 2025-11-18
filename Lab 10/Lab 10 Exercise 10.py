def make_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter

click_counter=make_counter()
print(click_counter())
print(click_counter())
print(click_counter())
