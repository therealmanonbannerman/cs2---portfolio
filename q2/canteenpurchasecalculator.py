# Calculating the overall price of the items

def calculate_total(price, quantity):
    total_cost = price * quantity
    return total_cost

# Calculating the change or the amount left to pay

def calculate_change(payment, total):
    return payment - total

# Gets the info from the purchaser

item_price = float(input("Please enter the amount of the item price: "))
item_quantity = int(input("Please enter the quantity: "))
amount_paid = float(input("Please enter the amount of money paid: "))

# Receives the overall cost adn keeps the returned value

total = calculate_total(item_price, item_quantity)

# Calculating the difference between the payment and overall price

difference = calculate_change(amount_paid, total)

# Shows the purchase info

print(f"Total Cost: PHP {total:.2f}")

if difference >= 0:
    print(f"Change: PHP {difference:.2f}")
else:
    print(f"Additional Amount Needed: PHP {-difference:.2f}")

# Documentation Questions:

# 1. calculate_total() multiplies the item price by the quantity.
#    calculate_change() subtracts the total cost from the payment.
#
# 2. # 2. Parameters are variables in the function definition.
#    Arguments are the actual values passed when calling the function.
#
# 3. The returned total is stored in the variable total.
#    It is then used in calculate_change() and displayed.
#
# 4. Separating the functions keeps the code organized and
#    makes each calculation easier to understand and reuse.
