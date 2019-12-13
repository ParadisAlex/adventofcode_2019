import math

def calculateFuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel

with open('day1_input.txt') as f:
    modules = [line.rstrip() for line in f]

fuel = 0
for i in modules:
    fuelReq = 0
    fuelCheck = calculateFuel(int(i))
    while fuelCheck > 0:
        fuelReq += fuelCheck
        fuelCheck = calculateFuel(fuelCheck)
    fuel += fuelReq
    
print(fuel)