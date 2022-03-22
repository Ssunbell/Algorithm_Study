n = int(input())
energydrinks_amounts = list(map(int, input().split()))
mixed_drink = max(energydrinks_amounts)
energydrinks_amounts.remove(mixed_drink)

for energydrinks_amount in energydrinks_amounts:
    mixed_drink += energydrinks_amount/2
print(mixed_drink)
