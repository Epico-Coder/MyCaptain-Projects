import json
n = str(input("List: "))
# Eg input: [5, -6, 7] or 5, -6, 7

# Parses string
try:
    n = json.loads(n)
except json.decoder.JSONDecodeError:
    n = n.split(",")
    n = [int(item) for item in n]

new_list = []

# Filters positive integers
try:
    for i in n:
        if i > 0:
            new_list.append(i)
except TypeError:
    print("Wrong input format!")

print(new_list)
