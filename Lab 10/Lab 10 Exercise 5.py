def double_it(x): return x*2
def capitalize_it(s): return s.upper()

def apply_to_all(items_list,operation_func):
    results=[]
    for item in items_list: results.append(operation_func(item))
    return results

print("Numbers doubled:",apply_to_all([1,5,10],double_it))
print("Strings capitalized:",apply_to_all(["hello","world"],capitalize_it))
