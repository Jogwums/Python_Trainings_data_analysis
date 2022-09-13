item_name = input("What do you want to sell?")
quantity = input(f"How many {item_name} do you want to sell ?")
price = input("What is the price of each item")
total = int(quantity) * int(price) # type conversion from str to int 

# feedback / output
output_msg = f"You are selling {quantity} pieces of {item_name} and you will get {price} per piece. Total price {total}"
print("*" * 10)
print(output_msg)