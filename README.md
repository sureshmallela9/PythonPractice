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

## 3. How can you concatenate two lists in Python?

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
