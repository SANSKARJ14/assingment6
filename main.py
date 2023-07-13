#ASSINGMENT 6
"""
#Q.1. What are keywords in python? Using the keyword library, print all the python keywords.

import keyword
keywords = keyword.kwlist
print(keywords)

"""

"""
Q.2. What are the rules to create variables in python?

Variable names can contain letters, digits, and underscores.
The first character of a variable name cannot be a digit.
Python keywords cannot be used as variable names.
Use descriptive and meaningful names for variables.
Assign values using the equals sign (=) operator.
"""

"""
Q.3. What are the standards and conventions followed for the nomenclature of variables in
python to improve code readability and maintainability?

(lowercase letters and underscores) for variable names.
Choose descriptive and meaningful names for variables.
Avoid single-letter variable names except for loop counters or mathematical formulas.
Uppercase letters with underscores are used for constants.
Avoid using Python keywords or built-in function names as variable names.

"""
"""
Q.4. What will happen if a keyword is used as a variable name?

it will result in a syntax error. 
Keywords are reserved words in the Python language that have predefined meanings and cannot be used as identifiers

"""
"""

Q.5. For what purpose def keyword is used
?
The def keyword in Python is used to define a function
he def keyword allows you to create your own functions with custom names, parameters
def keyword, you can modularize your code, promote reusability, and improve the organization and readability 
of your program.

"""
"""

Q.6. What is the operation of this special character ‘\’?

The backslash is used to create special characters or sequences. 
For example, \n represents a newline character, \t represents a tab character

"""
"""
Q.7. Give an example of the following conditions:
(i) Homogeneous list
(ii) Heterogeneous set
(iii) Homogeneous tuple

(i) Homogeneous list
A homogeneous list in Python is a list that contains elements of the same data type.

n = [1, 2, 3, 4, 5]

(ii) Heterogeneous set:

A heterogeneous set in Python is a set that can contain elements of different data types. 

(iii) Homogeneous tuple:
A homogeneous tuple in Python is a tuple that contains elements of the same data type. 

t = ("apple","banana","lichi")
"""
"""

Q.8. Explain the mutable and immutable data types with proper explanation & examples.

Mutable Data Types:

Mutable data types are those whose values can be modified after they are created. 
This means that you can change individual elements or properties of the object without creating a new object. 

my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

immutable data types 

those whose values cannot be changed once they are created. If you need to modify the value of an immutable object,
you have to create a new object.
Examples of immutable data types in Python include strings, numbers (integers, floats), and tuples.

my_list = (1, 2, 3)
my_list[0] = 10
print(my_list)  # Output: (1, 2, 3)
"""
"""
Q.9. Write a code to create the given structure using only for loop.
    *
   ***
  *****
 *******
*********

rows = 5

for i in range(rows):
    # Print spaces
    for j in range(rows - i - 1):
        print(" ", end="")

    # Print asterisks
    for k in range(2*i + 1):
        print("*", end="")

    # Move to the next line
    print()

"""
"""
Q.10. Write a code to create the given structure using while loop.
|||||||||
 |||||||
  |||||
   |||
    |

rows = 5
spaces = 0
asterisks = 9

while rows > 0:
    print(" " * spaces + "|" * asterisks)
    spaces += 1
    asterisks -= 2
    rows -= 1
"""
