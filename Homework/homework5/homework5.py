# ---3 Homework 1 + 2 Review---

# --3.1 Vocabulary Review--

# 1. Git is a version control system that keeps track of various files
# and versions of files, whereas GitHub is a cloud-based platform that uses Git
# to remotely store files and repositories
# 2. The Terminal is the system through which users can navigate their computer's
# programs using a number of commands, and the Command Line is the line in the
# terminal where the user types in commands
# 3. A local repository is stored within one's own machine, whereas a remote
# repository is stored on the web
# 4. Version control is a system that keeps track of programs and their various
# versions
# 5. The staging area is where changes are stored before being officially committed
# to their repository
# 6. git add stages changes to be committed
# 7. git commit records changes made to the repository
# 8. git push uploads changes to remote repository
# 9. git status provides information on everything going on in the working directory
# and staging area
# 10. git pull takes content from a remote repository and applies it to the local
# one; the opposite of git push
# 11. pwd prints working directory, telling you the complete file path to the directory
# you are looking at
# 12. ls lists items within the working directory
# 13. cd changes directory
# 14. nano allows the user to edit a file
# 15. touch creates a new file without opening it
# 16. mv moves a file to a specified place
# 17. rm removes a file
# 18. cat shows the contents of a file

# --3.2 A Directory Tree--

# pwd
# ls
# cd ../brianna_repo/,  git pull homework.py
# mv homework.py ../judy_decal/homework/
# cd ../judy_decal/homework/
# cat homework.py
# git add, git commit, git push origin main
# I don't think she called git pull correctly to locally save the changes from the
# remote repository.  She needs to call it once again to save these changes
# cd ~/Recent/

# ---4. Homework 3 Review---

# --4.1 Data Types--
def checkDataType(data):
    return type(data).__name__
print(checkDataType(3.14))
print(checkDataType(True))

# --4.2 Conditionals--
def evenOrOdd(intput):
    if intput % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(evenOrOdd(7))
print(evenOrOdd(10))

# ---5. Loops---
def sumWithLoop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))

# ---6. Homework 4 Review---

# --6.1 Lists--
def duplicateList(list):
    new_list = []
    for item in list:
        for i in range(2):
            new_list.append(item)   
    return new_list
print(duplicateList(["a", "b", "c"]))

# --6.2 Debugging
def square(num): # remember to include a colon when defining a function
    return num * num
print(square(12))

# ---7. Running Your Code---

# --7.2
def sumWithLoop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 2, 3, 4, 5]
print(sumWithLoop(numbers))
