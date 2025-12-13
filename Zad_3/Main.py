from House import House
from Flat import Flat

# Create a House
my_house = House(area=200, rooms=5, price=350000, address="123 Maple St", plot=500)

# Create a Flat
my_flat = Flat(area=80, rooms=3, price=150000, address="45 Oak Ave, Apt 12", floor=3)

# Print them
print(my_house)
print(my_flat)