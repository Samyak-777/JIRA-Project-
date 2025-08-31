def calculate_change(price):
    # Calculate change from a dollar (100 cents)
    change = 100 - price
    
    # Calculate coins using fewest coins approach (greedy algorithm)
    quarters = change // 25
    remaining_after_quarters = change % 25
    
    dimes = remaining_after_quarters // 10
    remaining_after_dimes = remaining_after_quarters % 10
    
    nickels = remaining_after_dimes // 5
    pennies = remaining_after_dimes % 5
    
    return change, pennies, nickels, dimes, quarters

# Hard-coded price as per problem statement
price = 67

change, pennies, nickels, dimes, quarters = calculate_change(price)

print(f"The price of your item is {price} cents, and your change is {change} cents.")
print("Here's the change that uses the fewest coins:")
print(f"pennies: {pennies}")
print(f"nickels: {nickels}")
print(f"dimes: {dimes}")
print(f"quarters: {quarters}")
