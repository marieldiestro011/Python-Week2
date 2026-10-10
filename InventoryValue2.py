products = []

while True:
    print("\n     ADD PRODUCT     ")
    
    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    
    #Store
    product = {
    "name": name,
    "price": price,
    "quantity": quantity
    }

    #Add dictionary to list
    products.append(product)
    
    print("Product added successfully!")

    #Ask users if they want to add more
    again = input("Add another product? (yes/no): ").lower()
    
    if again == "no" or again == "n":
        break
    
#Display Products
print("\n     PRODUCT INVENTORY     ")

total = 0

for product in products: 
    print("\nProduct:", product["name"])
    print("Price: ₱", product["price"])
    print("Quantity", product["quantity"])
    
    product_value = product["price"] * product["quantity"]
    total += product_value

print("\nTotal Products:", len(products))
print("Total Value: ₱", total)