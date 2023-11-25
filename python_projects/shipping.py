weight = 1.5

# Ground Shipping

if weight <= 2:
  cost_ground_shipping = 20 + weight * 1.50
elif weight <= 6:
  cost_ground_shipping = 20 + weight * 3
elif weight <= 10:
  cost_ground_shipping = 20 + weight * 4
else:
  cost_ground_shipping = 20 + weight * 4.75

print("Ground shipping: " + str(cost_ground_shipping))

# Ground Shipping Premiun

cost_ground_shipping_premium = 125.00

print("Ground shipping premium: " + str(cost_ground_shipping_premium))

# Drone Shipping

if weight <= 2:
  cost_drone_shipping = weight * 4.50
elif weight <= 6:
  cost_drone_shipping = weight * 9
elif weight <= 10:
  cost_drone_shipping = weight * 12
else:
  cost_drone_shipping = weight * 14.25

print("Drone shipping: " + str(cost_drone_shipping))

cheapest = cost_ground_shipping
if cheapest > cost_ground_shipping_premium:
  cheapest = cost_ground_shipping_premium
if cheapest > cost_drone_shipping:
  cheapest = cost_drone_shipping
print("Cheapest: " + str(cheapest))