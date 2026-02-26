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

