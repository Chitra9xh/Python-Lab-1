def process_item(price,code):
    assert isinstance(code,str),"Developer bug: discount_code must be a string"
    print("Processing item...")

process_item(100,"SAVE10")
process_item(100,10) 
