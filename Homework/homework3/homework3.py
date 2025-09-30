# 3 Print Functions

# 3.1 Say Goodbye

def say_goodby(name):
	print("Hello,", name)

# 3.2 Area of a Circle

def circle_area(radius):
	print(3.14 * (radius ** 2))



# 4 Return Functions

# 4.1 Subtract, Multiply, and Divide

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b



# 5 Conditionals

# 5.1 What Should I Wear?

readings = [15, 14, 17, 20, 23, 28, 20]

def high(readings):
	return max(readings)

def low(readings):
	return min(readings)

print(high(readings), low(readings))

# 5.2 Check if it's the Weekend

def is_weekend(day):
	if day == 6 or day == 7:
		return "It's the weekend!"
	else:
		return "It's not the weekend."

print(is_weekend(6))

# 5.3 Fuel Efficiency Calculator

def fuel_efficiency(miles, gallons):
	return (miles / gallons), "miles per gallon"

print(fuel_efficiency(20, 4))

# 5.4 Secret code

def encrypt(number):
	ten_power = len(str(number)) - 1
	return (number % 10) * (10 ** ten_power) + number // 10

print(encrypt(12345678))



# 6 Loops

# 6.1 Oski Stole Your Power

def exponent(x, y):
	new_x = 1
	for i in range(y):
		new_x = new_x * x
		i = i + 1
	return new_x

print(exponent(2, 5))

# 6.2 Min & Max with Loops

# 6.2.1 For Loops
def for_minimum(numbers_list):
	new_min = numbers_list[0]
	for i in range(len(numbers_list)):
		if numbers_list[i] < new_min:
			new_min = numbers_list[i]
		i = i + 1
	return new_min

print(for_minimum([12, 7, 4, 3, 5]))

def for_maximum(numbers_list):
	new_max = numbers_list[0]
	for i in range(len(numbers_list)):
		if numbers_list[i] > new_max:
			new_max = numbers_list[i]
		i = i + 1
	return new_max

print(for_maximum([4, 7, 6, 11, 14, 2]))

# 6.2.2 While Loops
def while_min(numbers_list):
	new_min = numbers_list[0]
	i = 0
	while i < len(numbers_list):
		if numbers_list[i] < new_min:
			new_min = numbers_list[i]
		i = i + 1
	return new_min

print(while_min([12, 7, 4, 3, 5]))

def while_max(numbers_list):
	new_max = numbers_list[0]
	i = 0
	while i < len(numbers_list):
		if numbers_list[i] > new_max:
			new_max = numbers_list[i]
		i = i + 1
	return new_max

print(while_max([4, 7, 6, 11, 14, 2]))

# 6.3 Calculate the Sum
def digit_sum(number):
	total = 0
	while number > 0:
		total += number % 10
		number //= 10
	return total

print(digit_sum(2468))



# 7 Running Your Script

# 7.1

number = 12345678
result = encrypt(number) # same number but with the last digit first

print(f"The result of Secret Code (5.1) with number = {number} is {result}")