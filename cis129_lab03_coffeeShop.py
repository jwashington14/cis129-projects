#Program: Coffee Shop Simulator (Extended) 
#Description: A simple interactive text-based coffee shop simulator that calculates the receipt based on customer input
#Author:Jessica Washington
#Date:10/14/2024

# Constsants

COFFEE_PRICE = 5.00
MUFFIN_PRICE = 4.00
CHAI_TEA_PRICE = 3.00
MACARRON_PRICE = 3.50
TAX_RATE = 0.06

#Input: Number of coffees, muffins, chai teas, and macarrons the user is purchasing

num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_chai_teas = int(input("Number of chai_teas bought? "))
num_macarrons = int(input("Number of macarrons bought? "))

# Calculate subtotals
subtotal_coffee = num_coffees * COFFEE_PRICE
subtotal_muffin = num_muffins * MUFFIN_PRICE
subtotal_chai_tea = num_chai_teas * CHAI_TEA_PRICE
subtotal_macarron = num_macarrons * MACARRON_PRICE
subtotal = subtotal_coffee + subtotal_muffin + subtotal_chai_tea + subtotal_macarron

# Calculate tax
tax = subtotal * TAX_RATE

# Calculate total
total = subtotal + tax

# Output: Display the receipt
print("\n********************************************************************************")
print("Welcome to Sip Slow Cafe")
print("********************************************************************************")
print(f"{num_coffees} Coffee(s) at ${COFFEE_PRICE:.2f} each: ${subtotal_coffee:.2f}")
print(f"{num_muffins} Muffin(s) at ${MUFFIN_PRICE:.2f} each: ${subtotal_muffin:.2f}")
print(f"{num_chai_teas} Chai Tea(s) at ${CHAI_TEA_PRICE:.2f} each: ${subtotal_chai_tea:.2f}")
print(f"{num_macarrons} Macarron(s) at ${MACARRON_PRICE:.2f} each: ${subtotal_macarron:.2f}")
print(f"6% tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("********************************************************************************")
print("\nThanks for visiting us! Tell us how we did! Text "'"KYOTO DRIP"'" to DECAF (33223) to take our survey within 7 days for 10% off your next purchase!")



