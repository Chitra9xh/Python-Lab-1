def calculate_item_price(quantity, price_per_unit):
    return quantity*price_per_unit

q=int(input("Enter quantity: "))
p=float(input("Enter price per unit: "))
total_cost=calculate_item_price(q,p)
print(f"Total cost for {q} items at {p} each is {total_cost}")
