print("--------------------------------------------------")
itemCode = input("Enter Item Code : ")
itemCategory = input("Enter Item Category : ")
item_name = input("Enter Item Name : ")
unit_price = int(input("Enter Unit Price : "))
customer_buy = input("Enter Customer Buy : ")
qty = int(input("Enter Item qty : "))
discount_percentage = int(input("Enter Item Discount : "))
item_discount = unit_price * discount_percentage/100
print("-------------------------------------------------")
item_total_price = unit_price * qty
net_amount = item_discount * qty
current_stock = qty
customer_buy = int(input("Enter Item Qty : "))
available_stock = current_stock - customer_buy


print("Item Code: ", itemCode)
print("Item Category: ", itemCategory)
print("Item Name: ", item_name)
print("Item Unit Price: ", unit_price)
print("Item Quantity: ", qty)
print("Item Discount Percentage: ", discount_percentage)
print("Item Discount: ", item_discount)
print("Item Total Price: ", item_total_price)
print("Item Net Amount: ", net_amount)
print("Current Stock: ", current_stock)
print("Customer Needs: ", customer_buy)
print("StockmAfter Selling: ", available_stock)

                   

