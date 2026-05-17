# Python Interview Questions

## 1. Is Python a Compiled Language or an Interpreted Language?

Whether a language is compiled, interpreted, or both is **not defined by the language standard**. In other words, it is **not an inherent property of a programming language**.  
Different Python distributions (or implementations) choose to do different things—compile, interpret, or both.

However, the most common implementation, **CPython**, uses **both compilation and interpretation**, but at different stages of execution.

---

### Compilation Phase

When you write Python code and run it, the source code (`.py` files) is first **compiled into an intermediate form called bytecode** (`.pyc` files).

- Bytecode is a lower-level representation of your code  
- It is **not machine code**  
- It is designed to be executed by the **Python Virtual Machine (PVM)**

---

### Interpretation Phase

After compilation to bytecode, the Python Virtual Machine (**PVM**) executes the bytecode.

- The PVM acts as an **interpreter**  
- It reads and executes bytecode **instruction by instruction at runtime**  
- This runtime execution is why Python is commonly called an **interpreted language**

---

### Other Implementations

Some Python implementations use additional techniques:

- **PyPy** uses **Just-In-Time (JIT) compilation**  
- JIT compiles Python bytecode into **machine code at runtime**  
- This improves performance and **blurs the line between compiled and interpreted languages**

---

### Conclusion

Python is best described as a **hybrid language**:

- **Compiled** to bytecode  
- **Interpreted** by the Python Virtual Machine  
- Some implementations also **JIT compile** to machine code

---

## 2. How can you concatenate two lists in Python?

There are multiple ways to concatenate two lists in Python:

### Using the `+` Operator

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
```

### Using the extend() 

```python

list1.extend(list2)
```
---

## 3.Difference between for loop and while loop in Python?

### ForLoop:
Used when we know how many times to repeat, often with lists, tuples, sets, or dictionaries.
```python
for i in range(5):
    print(i)
```

### While Loop:
Used when we only have an end condition and don’t know exactly how many times it will repeat.
```python
c = 0
while c < 5:
    print(c)
    c += 1
```
---
## 4. How do you floor a number in Python?

To floor a number in Python, you can use the math.floor() function, which returns the largest integer less than or equal to the given number.
### floor():
method in Python returns the floor of **x** i.e., the largest integer not greater than **x**
```python
import math

n = 3.7
F_num = math.floor(n)

print(F_num)

output: 3
```
---

## 5. How do you ceil a number in Python?
### ceil():

math.ceil() function returns the smallest integer greater than or equal to a given number. It always rounds a value upward to the nearest whole number. If the input is already an integer, the same value is returned.

This example shows how math.ceil() rounds a positive decimal number up to the next integer.

```python
import math

x = 33.7
res = math.ceil(x)
print(res)

output: 34 # if input is 33.1 then output would be same:34
```
---


## 6. Is Indentation Required in Python?

Yes, **indentation is required in Python**.

### What is Indentation?

Indentation refers to the **spaces or tabs at the beginning of a line of code**.  
In Python, indentation is used to **define blocks of code** instead of curly braces `{}` (as used in languages like C, C++, or Java).

---

### Why is Indentation Important?

- It tells Python **which statements belong to a block**
- It improves **code readability**
- Incorrect indentation causes an **IndentationError**

---

### Example with Correct Indentation

```python
if True:
    print("This is indented correctly")
    print("Python uses indentation")
```
---


## 6.What is the difference between / and // in Python?

**/** represents precise division (result is a floating point number) whereas **//** represents floor division (result is an integer). For Example:


```python
print(5//2)
print(5/2)

output: 
2
2.5
```
---
## 7. Can we Pass a function as an argument in Python?

Yes, Several arguments can be passed to a function, including objects, variables (of the same or distinct data types) and functions.
Functions can be passed as parameters to other functions because they are objects.
Higher-order functions are functions that can take other functions as arguments.


```python
def add_func(a, b):
    return a + b

def apply_func(func, a, b):
    return func(a, b)

print(apply_func(add_func, 1, 2))
```
---
## 8. What is a dynamically typed language?

- In a dynamically typed language, the data type of a variable is determined at runtime, not at compile time.
- No need to declare data types manually; Python automatically detects it based on the assigned value.
- Examples of dynamically typed languages: Python, JavaScript.
- Examples of statically typed languages: C, C++, Java.
- Dynamically typed languages are easier and faster to code.
- Statically typed languages are usually faster to execute due to type checking at compile time.

```python
x = 10       # x is an integer
x = "Hello"  # Now x is a string
```
- Here, the type of x changes at runtime based on the assigned value hence it shows dynamic nature of Python.
---

## 9. What is pass in Python?

- The pass statement is a placeholder that does nothing.
- It is used when a statement is syntactically required but no code needs to run.
- Commonly used when defining empty functions, classes or loops during development.
```python
def fun():
    pass  # Placeholder, no functionality yet

# Call the function
fun()

# No Output
# Here, fun() does nothing, but the code stays syntactically correct.
```
---

## 10. How are arguments passed by value or by reference in Python?

- Python’s argument-passing model is neither “Pass by Value” nor “Pass by Reference” but it is “Pass by Object Reference”. 
- Depending on the type of object you pass in the function, the function behaves differently. Immutable objects show “pass by value” whereas mutable objects show “pass by reference”.
- You can check the difference between pass-by-value and pass-by-reference in the example below:
### Mutability matters:

- Mutable objects (like lists, dictionaries, sets) can be changed inside the function, and those changes will be visible outside.

- Immutable objects (like integers, strings, tuples) cannot be altered in place. Reassigning them inside the function only changes the local reference, not the original object.
```python
def call_by_val(x):
    x = x * 2
    return x


def call_by_ref(b):
    b.append("D")
    return b


a = ["E"]
num = 6

# Call functions
updated_num = call_by_val(num)
updated_list = call_by_ref(a)

# Print after function calls
print("Updated value after call_by_val:", updated_num)
print("Updated list after call_by_ref:", updated_list)

#output
#Updated value after call_by_val: 12
#Updated list after call_by_ref: ['E', 'D']
```
---

## 11. What is a lambda function?

- A lambda function is an anonymous function. This function can have any number of parameters but, can have just one statement.
```python
s1 = 'testLamda'

s2 = lambda func: func.upper()
print(s2(s1))

#output : TESTLAMDA

```
---
## 12. What are *args and **kwargs?

### *args:

- **Purpose:** Allows a function to accept any number of keyword arguments.
- **Data type:** Stored as a dictionary.

```python
def fun(*argv):
    for arg in argv:
        print(arg)

fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

#o/p:
#Hello
#Welcome
#to
#GeeksforGeeks

```

### *kwargs: 

- **Purpose:** Allows a function to accept any number of keyword arguments.
- **Data type:** Stored as a dictionary.
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Suresh", age=25, city="Hyderabad")


#o/p: - Here, kwargs becomes {'name': 'Suresh', 'age': 25, 'city': 'Hyderabad'}.

```
---

## 13. What is List Comprehension? Give an Example.

- List comprehension is a way to create lists using a concise syntax. It allows us to generate a new list by applying an expression to each item in an existing iterable (such as a list or range).

### Example: 

if we have a list of integers and want to create a new list containing the square of each element, we can easily achieve this using list comprehension.

```python
a = [2,3,4,5]
list_new = [val ** 2 for val in a]
print(list_new)

#o/p: [4, 9, 16, 25]

```
---

## 14. What is a break, continue and pass in Python? 

### Break:
Break statementis used to terminate the loop or statement in which it is present. After that, the control will pass to the statements that are present after the break statement, if available.

### Continue: 
Continue is also a loop control statement just like the break statement. continue statement is opposite to that of the break statement, instead of terminating the loop, it forces to execute the next iteration of the loop.
### Pass:
Pass means performing no operation or in other words, it is a placeholder in the compound statement, where there should be a blank left and nothing has to be written there.

---

## 15. What is the difference between a Set and Dictionary?

### Set:
- A Python Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set.
- Syntax: Defined using curly braces {} or the set() function.


```python
my_set = {1, 2, 3}
```

### Dictionary:
- Dictionary in Python is an ordered (since Py 3.7) [unordered (Py 3.6 & prior)] collection of data values
- used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair.
- Key-value is provided in the dictionary to make it more optimized.
- Defined using curly braces {} with key-value pairs.
```python
my_dict = {"a": 1, "b": 2, "c": 3}
```
---

## 16. What are Built-in data types in Python?

- ***Numeric:*** The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, a Boolean, or even a complex number.
- ***Sequence Type:*** The sequence Data Type in Python is the ordered collection of similar or different data types. There are several sequence types in Python:
    - Python String
    - Python List
    - Python Tuple
    - Python range
- ***Mapping Types:*** In Python, hashable data can be mapped to random objects using a mapping object. There is currently only one common mapping type, the dictionary and mapping objects are mutable.
  - Python Dictionary
- **Set Types:** In Python, a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
---

## 17. What is the difference between a Mutable datatype and an Immutable data type?

- Mutable data types can be edited i.e., they can change at runtime. Eg – List, Dictionary, etc.
- Immutable data types can not be edited i.e., they can not change at runtime. Eg – String, Tuple, etc.

```python

s = "hello"
s[0] = "H"   # ❌ Error: 'str' object does not support item assignment

s = "H" + s[1:]   # ✅ Creates a new string "Hello"


t = (1, 2, 3)
t[0] = 10   # ❌ Error: 'tuple' object does not support item assignment

t = (10,) + t[1:]   # ✅ New tuple (10, 2, 3)
```
---

## 18. What is a Variable Scope in Python?

"The location where we can find a variable and also access it" is nothing but  scope of a variable.

### Python Local variable:
- Local variables are those that are initialized within a function and are unique to that function. A local variable cannot be accessed outside of the function.
```python
  def my_function():
      x = 10   # local variable
      print("Inside function:", x)
  
  my_function()
  print(x)   # ❌ Error: NameError (x not defined outside)
```
### Python Global variables:
- Global variables are the ones that are defined and declared outside any function and are not specified to any function.
```python
y = 20   # global variable

def my_function():
    print("Inside function:", y)  # can access global

my_function()
print("Outside function:", y)     # also accessible here
```
### Module-level scope:
- It refers to the global objects of the current module accessible in the program.
```python
# file: mymodule.py
z = 30   # module-level variable

def show():
    print("Module-level variable:", z)

# If you import this module elsewhere:
# import mymodule
# print(mymodule.z)   # accessible
```
### Outermost scope:
- It refers to any built-in names that the program can call. The name referenced is located last among the objects in this scope.
```python
# These are names built into Python itself — always available without import.
# Example of built-in scope
print(len([1, 2, 3]))   # len is a built-in function
print(sum([1, 2, 3]))   # sum is also built-in
```
---
## 19. How is a dictionary different from a list?

- A list is an ordered collection of items accessed by their index, While a dictionary is an unordered collection of key-value pairs accessed using unique keys.
- Lists are ideal for sequential data, whereas dictionaries are better for associative data. For example, a list can store [10, 20, 30], whereas a dictionary can store {"a": 10, "b": 20, "c": 30}.
---

## 20. What is docstring in Python?

Python documentation strings (or docstrings) provide a convenient way of associating documentation with Python modules, functions, classes and methods.

***Declaring Docstrings:*** The docstrings are declared using ”’triple single quotes”’ or “””triple double quotes””” just below the class, method, or function declaration. All functions should have a docstring.

***Accessing Docstrings:*** The docstrings can be accessed using the `__doc__` method of the object or using the help function.

```python
def add_numbers(a, b):
    """
    This function takes two numbers as input
    and returns their sum.
    """
    return a + b

# Accessing the docstring
print(add_numbers.__doc__)
# o/p: This function takes two numbers as input and returns their sum.
```
---

## 21. How is Exceptional handling done in Python?

There are 3 main keywords i.e. try, except and finally which are used to catch exceptions:

- **try:** A block of code that is monitored for errors.
- **except:** Executes when an error occurs in the try block.
- **finally:** Executes after the try and except blocks, regardless of whether an error occurred. It’s used for cleanup tasks.
- Trying to divide a number by zero will cause an exception.
```python
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
    
except ZeroDivisionError:
    print("Can't be divided by zero!")
```
---
## 22. What is the difference between Python Arrays and Lists?
### Arrays:
- Arrays are specifically used to store a collection of numeric elements that are all of the same type. This makes them more efficient for storing large amounts of data and performing numerical computations where the type consistency is maintained.
- Need to import the array module to use arrays.
```python
from array import array
arr = array('i', [1, 2, 3, 4])  # Array of integers
```

### List:
- Lists are more flexible than arrays in that they can hold elements of different types (integers, strings, objects, etc.). They come built-in with Python and do not require importing any additional modules.
- Lists support a variety of operations that can modify the list
```python
a = [1, 'hello', 3.14, [1, 2, 3]]
```
---
## 23. What are Modules and Packages in Python?
### Module:
- A module is a single file that contains Python code (functions, variables, classes) which can be reused in other programs. You can think of it as a code library. For example: math is a built-in module that provides math functions like sqrt(), pi, etc.
```python
import math
print(math.sqrt(16))
```
### Package:
- package is a collection of related modules stored in a directory. It helps in organizing and grouping modules together for easier management. For example: The numpy package contains multiple modules for numerical operations.

- To create a package, the directory must contain a special file named __init__.py.

---

## 24. What is the difference between xrange and range functions?

- range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python.
- In Python 3, there is no xrange, but the range function behaves like xrange.
### Range: 
-Returns a list of numbers and Uses more memory for large ranges.
```python
nums = range(5)
print(nums)
# [0, 1, 2, 3, 4]
```
### XRange: 
- Returns an iterator-like object (lazy sequence).
- Generates numbers one at a time.
- Much more memory efficient.
```python
When a loop asks for the next value
```
### In Python 3: 

- xrange() was removed.
- range() in Python 3 behaves like Python 2's xrange():
```python
lazy
memory efficient
iterable
fast
```
---
## 25. What is Dictionary Comprehension? Give an Example

### Dictionary Comprehension:
is a syntax construction to ease the creation of a dictionary based on the existing iterable.

```python
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  

# this line shows dict comprehension here  
d = { k:v for (k,v) in zip(keys, values)}  

# We can use below too
# d = dict(zip(keys, values))  

print (d)
```
---
