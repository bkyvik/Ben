# File: homework1. py



#  --- 3.1 Variables and Data Types ---

a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print(b)
print(type(b)) # b is a float, a value with decimals

c = 3j
print(c)
print(type(c)) # c is a complex number, a number with an imaginary component

d = "hello"
print(d)
print(type(d)) # d is a string, a series of characters

e = [1, 2, 3]
print(e)
print(type(e)) # e is a (integer) list, an ordered, mutable (modifyable) collection of objects

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, an unordered collection of corresponding pairs

g = (1, 2)
print(g)
print(type(g)) # g is a tuple, an ordered immutable (unchangeable) collection of objects

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a (string) list, an ordered, mutable collection of objects

i = True
print(i)
print(type(i)) # i is a boolean, a binary true or false value

j = None
print(j)
print(type(j)) # j is a none type, meaning it has no value or data type

k = [True, "blue", 12]
print(k)
print(type(k)) # k is a (multiple data type) list, an ordered, mutable collection of objects

l = str(14)
print(l)
print(type(l)) # l is a string, a series of characters

m = 1e4
print(m)
print(type(m)) # m is a float, a number with a decimal point

# 1. I counted 9 data types (including nonetype)
# 2. integer, float, complex, string, list, dictionary, tuple, boolean, nonetype
# 3. variables b and m are both floats, d and l are strings, and e h and k are all lists, though they store different data types
# 4. l was a string, because it was defined using the string function, which changes data types into strings.
# It's the same as saying l = "14".  The computer does not see l as the number 14, just as the symbols  that represent it.  I'd get an error if I tried to use l to do math
# 5

n = {1, 2, 3, 4}
print(n)
print(type(n)) # n is a set, an unordered collection of unique objects



# --- 3.2 Booleans ---

print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 does not equal 9
print(bool("abc")) # True, defined input
print(bool(123)) # True, defined input
print(bool(["apple", "cherry", "banana"])) # True, defined input
print(bool(True)) # True, true is true
print(bool(False)) # False, false is false
print(bool(0)) # False, zero has no value
print(bool("")) # False, no value
print(bool(" ")) # True, contains input
print(bool(())) # False, no input
print(bool([])) # False, no input
print(bool({})) # False, no input
print(bool(True and False)) # False, can't be true and false
print(bool(True and True)) # True, true is true
print(bool(False and False)) # False, false is false
print(bool(True or False)) # True, since one is true
print(bool(True or True)) # True, since one is true
print(bool(False or False)) # False, since both are false
print(bool(not(False))) # True, if it ain't false, it's true
print(bool(not(True))) # False, likewise
print(3 == 3)
print("3" == 3)

# 1. I noticed that all the true functions were either verifiably correct, or contained something meaningful
# 2. I was surprised by the result of bool((0)) because it seemed like something of an exception to the boolean rules for integers
# 3. The expression (3 == 3) is true because it is a 1 for 1 comparison of the same object
# 4. The expression ("3" == 3) is false because "3" is a string and 3 is an integer, so they are not comparable



# --- 3.3 Operators ---

# 3.3.1 Arithmetic Operators
print(10 + 5) # 15, + performs addition
print(10 - 5) # 5, - performs subtraction
print(2 * 4) # 8, * performs multiplication
print(6 / 3) # 2.0, / performs float division
print(5 % 2) # 1, % mod finds remainder of division
print(3 ** 2) # 9, ** performs exponentiation
print(15 // 2) # 7, // performs or floor division (rounds down to next integer)

# 3.3.2 Comparison Operators
print(5 == 2) # False, == verifies equivalence
print(10 != 10) # False, != verifies nonequivalence
print(2 < 5) # True, < verifies less than
print(12 > 5) # True, > verifies greater than
print(5 <= 6) # True, <= verifies less than or equal to
print(1 >= 10) # False, >= verifies greater than or equal to

# 3.3.3 Assignments Operators FIX BEFORE SUBMITTING
x = 5
x += 5
print(x)
x -= 4
print(x)
x *= 3
print(x)

# 3.3.4 Logical Operators
# 1. The operator and returns the boolean value True only if both values are true.
# ((5 == 5) and (1 == 1)) is True, since both are true
# ((5 == 5) and (1 == 5)) is False, since at least one is false
# 2. The operator or returns the boolean value True if either value is true.
# ((5 == 5) or (1 == 5)) is True, since at least one value is true.
# ((5 == 6) or (5 == 7)) is False, since both values are false
# 3. The operator not returns the boolean value opposite to the statement in question
# y = False
# (not y) is True, since y is false
# z = True
# (not z) is False, since y is true

# More Questions:
# 1. / deals with floats, // deals with integers, rounding down if necessary (floor division)
# 2. % finds the remainder, // finds the divided part (the principal, if you will)
# 3. I'd use the mod % operator to find the remainder. 13 % 4 = 1
# 4. Assignment operators assign a new value to a variable based on its current value



# --- 3.4 Strings ---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # Prints: l
print(my_string[4]) # Prints: o
print(my_string[-1]) # Prints: o
print(my_string[1 : 3]) # Prints: el
print(my_string[0 : 5 : 2]) # Prints: hlo
print(len(my_string)) # Prints: 5
print(my_string + "goodbye") # Prints: hellogoodbye
print(my_string * 7) # Prints: hellohellohellohellohellohellohello

# 3.4.1 Questions:
# 1. Slicing is the breaking up of a string into certain characters.
# I sliced my string on lines 154-161.
name = "Oski"
print("Hello, my name is", name)
# 2. Prints: Hello, my name is Oski
name = "Oski"
print(f"Hello, my name is", {name})
# 3. Prints: Hello, my name is {'Oski'}
# 4. The first statement inserted a variable into the output
# The second statement, an f-string, inserted a whole expression into the output

# --- 3.5 Terminal Commands ---
# 1. cd
# Changes directories. Use it to move from one folder to another
# Example. cd Desktop
# 2. ls
# Lists contents.  Use it to see what's in folder
# Example ls
# 3. ls -a
# Lists all folder contents, including hidden ones
# Example. ls -a
# 4. mkdir
# Makes directory
# Example. mkdir homework_directory
# 5. cat
# Concatenate. shows file contents
# Example. cat script.py
# 6. pwd
# Print working directory.  Shows what current folder you're in
# Example. pwd
# 7. cd ..
# Exits to parent directory.  Use it to get out of inner folder while staying in outer folder
# Example. cd ..
# 8. cd . 
# Keeps the exact same directory.  No useful applications
# Example cd .
# 9. cd ~
# Changes to home directory.  Use to get out of all folders
# Example. cd ~
# 10. cp
# Makes copy with new name.  Use it to duplicate files
# Example. cp script.py scriptcopy.py
# 11. mv
# Move.  Use it to move files into other directories
# Example. mv scriptcopy.py homework_directory
# 12. rm
# Remove.  Use it to get rid of files
# Example. rm scriptcopy.py
# 13. clear
# Clears terminal.  Use it to get all the text off your screen
# Example. Clear
# 14. grep
# Find in file.  Use it to see where something occurs in a file
# Example. grep "comment" script.py

# Questions
# 1. whoami
# Tells me my username
# Example. whoami
# date
# Tells me the date and time
# Example. date
# touch
# Creates file
# Example. touch newfile
# 2. ls only shows visible files whereas ls -a shows hidden files as well
# 3. A hidden file is a file that the operating system does not show
# 4. rm ./*
# Removes everything in current directory
"""
Example. rm./*
rm -r
Remove directory
Example rm -r homework_directory
rm -rf
Removes directory and contents
Example. rm -rf homework_directory
"""