with open(r'input.txt', 'r') as file:
    input = file.read().strip().split('\n')

def fuel_required(weight):
    return max((weight // 3) - 2, 0)

print("Day 1, Part 1 :", sum([fuel_required(int(x)) for x in input]))

def fuel_extra_weight(weight):
    fuel_req = max((weight // 3) - 2, 0)
    if fuel_req == 0: return 0
    return fuel_req + fuel_extra_weight(fuel_req)

print("Day one, Part 2 :", sum([fuel_extra_weight(int(x)) for x in input]))