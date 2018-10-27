import random

number = 0
try:
    number = int(input("Number of runs: "))
except ValueError:
    print("Not a number")
    exit(255)

heads = 0
for x in range(number):
    result = random.choice([True, False])
    if result:
        print("Heads")
        heads += 1
    else:
        print("Tail")

print("Heads: " + str(round(heads / number * 100, 2)) + "% Tails: " + str(
    round((number - heads) / number * 100, 2)) + "%")
