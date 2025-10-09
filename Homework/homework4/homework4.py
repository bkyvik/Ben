# 3. Lists

# 3.1 List Operations
favorite_foods = ["peanut butter", "yogurt", "bagel", "potato", "yam"]

print(favorite_foods[1])

print(favorite_foods[-1])

favorite_foods.append("beans")

favorite_foods.insert(0, "apple")

del favorite_foods[2]

print(len(favorite_foods))

for food in favorite_foods:
    print(food.upper())

first_and_last_foods = favorite_foods[1:-1:-1]
print(first_and_last_foods)

if "potato" in first_and_last_foods:
    print("A potato!")
else:
    print("No potato!")

if "potato" in favorite_foods:
    print("A potato!")
else:
    print("No potato!")

# 3.2 Slicing and Striding
numbers = list(range(20))

def get_first_15(numbers):
    return numbers[:16:]
print(get_first_15(numbers))

def get_every_5th(list):
    return(list[::5])
print(get_every_5th(get_first_15(numbers)))

def reverse_and_stride(list):
    new_list = list[::-1]
    return(new_list[::3])
print(reverse_and_stride(get_every_5th(get_first_15(numbers))))

# 3.3 Nested Lists

# 3.3.1 Nested List Operations
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(numbers[2][::])

print(numbers[2][2])

numbers.append([10, 11, 12])

def sum_nested(list):
    total = 0
    for sublist in list:
        for item in sublist:
            total += item
    return total
print(sum_nested(numbers))

# 3.4

five_by_five = [[i
    for i in range(j, j + 5)]
        for j in range(1, 25, 5)
]
print(five_by_five)

def replace_threes(list):
    list_no_threes = []
    for sublist in list:
        for item in sublist:
            sublist_no_threes = []
            if item % 3 == 0:
                sublist_no_threes.append("?")
            else:
                sublist_no_threes.append(item)

            list_no_threes.append(sublist_no_threes)
    return list_no_threes
threeless_list = replace_threes(five_by_five)
print(threeless_list)

def threeless_sum(list):
    total = 0
    for sublist in list:
        for item in sublist:
            if item != "?":
                total += item
    return total
running_out_of_names = threeless_sum(threeless_list)
print(running_out_of_names)

# 4 Dictionaries

# 4.1 Dicionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])

ages["Mira"] = 100

ages["Milana"] = 52

for key, value in ages.items():
    print(f"{key}: {value}")

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sum_nested(list):
    total = 0
    for sublist in list:
        for item in sublist:
            total += item
    return total
print(sum_nested(numbers))

import homework4 as h4

