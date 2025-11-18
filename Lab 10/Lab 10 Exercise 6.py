def is_even(n): return n%2==0
def is_long_word(s): return len(s)>5

def filter_list(items_list,test_func):
    passed_items=[]
    for item in items_list:
        if test_func(item): passed_items.append(item)
    return passed_items

print("Even numbers:",filter_list([1,2,3,4,5,6],is_even))
print("Long words:",filter_list(["hi","python","cse","function"],is_long_word))
