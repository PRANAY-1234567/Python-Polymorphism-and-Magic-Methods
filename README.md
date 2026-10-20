# Python Polymorphism and Magic Methods

## 📌 Overview

This project demonstrates important concepts of Object-Oriented Programming (OOP) in Python, including duck typing, polymorphism, operator overloading, magic methods, inheritance, method overloading, and constructor overloading.
The examples explain how different objects can share the same method name, how operators can work with user-defined objects, and how Python handles methods with varying arguments.

## 🎯 Concepts Covered

* Duck Typing
* Polymorphism
* Operator Overloading
* Magic Methods (Dunder Methods)
* Single Inheritance
* Method Overriding
* Method Overloading
* Default Parameters
* Variable Positional Arguments (`*args`)
* Variable Keyword Arguments (`**kwargs`)
* Constructor Overloading

---

## 📂 Examples Included

### 1. Duck Typing

Duck typing is a Python programming concept in which an object's suitability is determined by its behavior rather than its class or inheritance relationship.

In your example, the `Dog`, `cat`, and `Goat` classes each define a `sound()` method.

```python
class Dog:
    def sound(self):
        print("Bark....")

class cat:
    def sound(self):
        print("Meow...")

class Goat:
    def sound(self):
        print("Goat")

def animal(x):
    x.sound()
```

The `animal()` function accepts different objects and calls their `sound()` methods.

**Key learning:** Objects do not need to inherit from the same parent class as long as they provide the expected behavior.

### 2. Duck Typing Using a Loop

This example demonstrates how a loop can call the same method on different objects.

**Classes:**

* `Bike`
* `Class`
* `Car`
* `Engine`

Each class defines a `start()` method.

```python
w = [Bike(), Class(), Car(), Engine()]

for i in w:
    i.start()
```

**Output:**

```text
Bike Started
Class Started
Car Started
Engine Started
```

**Key learning:** Different objects can respond to the same method call in their own way without requiring a shared inheritance hierarchy.

### 3. Operator Overloading

Operator overloading allows operators such as `+`, `-`, `*`, and `/` to work with user-defined objects by implementing special methods.

For example, the `Point` class stores a page count.

```python
class Point:
    def __init__(self, Pages):
        self.p = Pages
```

If you try to add two `Point` objects without defining addition behavior, Python raises a `TypeError`.

To support addition, you can implement the `__add__()` method.

### 4. Magic Methods or Dunder Methods

Magic methods are special methods whose names begin and end with double underscores.

Examples include:

| Magic Method    | Purpose                                     |
| --------------- | ------------------------------------------- |
| `__init__()`    | Initializes an object                       |
| `__add__()`     | Defines behavior for `+`                    |
| `__sub__()`     | Defines behavior for `-`                    |
| `__mul__()`     | Defines behavior for `*`                    |
| `__truediv__()` | Defines behavior for `/`                    |
| `__gt__()`      | Defines behavior for `>`                    |
| `__lt__()`      | Defines behavior for `<`                    |
| `__eq__()`      | Defines behavior for `==`                   |
| `__pow__()`     | Defines behavior for `**`                   |
| `__str__()`     | Defines a readable string representation    |
| `__repr__()`    | Defines a developer-oriented representation |

### 5. Addition Using `__add__()`

The `Operation` class demonstrates how to add the values stored in two objects.

```python
class Operation:
    def __init__(self, book):
        self.b = book

    def __add__(self, other):
        return self.b + other.b
```

Example:

```python
a = Operation(100)
b = Operation(200)

print(a + b)
```

**Output:**

```text
300
```

Python calls `a.__add__(b)` when evaluating `a + b`.

### 6. Returning an Object from Operator Overloading

In another example, `__add__()` returns a new `Operation` object rather than returning a number.

```python
def __add__(self, other):
    return Operation(self.b + other.b)
```

The `__repr__()` method is then used to provide a readable representation of the result.

**Key learning:** An overloaded operator can return a value or another object, depending on the implementation.

### 7. Subtraction Using `__sub__()`

The `Data` class demonstrates subtraction between objects.

```python
class Data:
    def __init__(self, a):
        self.a = a

    def __sub__(self, other):
        return Data(self.a - other.a)

    def __str__(self):
        return f'{self.a}'
```

Example:

```python
d = Data(12)
d1 = Data(10)

print(d - d1)
```

**Output:**

```text
2
```

The `__sub__()` method creates a new object containing the difference, while `__str__()` controls how that object is displayed by `print()`.

### 8. Multiple Operator Overloading

The `AllOperation` class stores two numeric values, `a` and `b`.

It implements the following operators:

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)

Each method performs the corresponding operation on both attributes and returns a tuple containing the results.

Example:

```python
x = AllOperation(100, 200)
y = AllOperation(50, 100)

print(x + y)
print(x - y)
print(x * y)
print(x / y)
```

**Output:**

```text
(150, 300)
(50, 100)
(5000, 20000)
(2.0, 2.0)
```

### 9. Comparison and Power Operators

The extended `AllOperation` class also implements:

* Greater than (`>`)
* Less than (`<`)
* Equal to (`==`)
* Power (`**`)

For example:

```python
x = AllOperation(1, 3)
y = AllOperation(6, 2)

print(x > y)
print(x < y)
print("Equal To", x == y)
print("Power Factor", x ** y)
```

**Output:**

```text
(False, True)
(True, False)
Equal To (False, False)
Power Factor (1, 9)
```

**Important:** In this implementation, comparison methods return tuples because they compare the two attributes separately. Therefore, `x == y` returns a tuple rather than a single Boolean value. This differs from conventional equality behavior, where `==` normally returns one Boolean.

### 10. Single Inheritance: Bank and ICICI Bank

The `Bank` class stores customer and bank information:

* Customer name
* Branch
* IFSC code
* Location

The `ICIC_BANK` class inherits from `Bank` and adds PAN card and Aadhaar number attributes.

```python
class ICIC_BANK(Bank):
    def __init__(self, pan_card_number, aadhar_number):
        super().__init__(
            cname="Naman",
            Branch="Delhi",
            IFSC=100,
            location="Metro"
        )
        self.pan_card_number = pan_card_number
        self.aadhar_number = aadhar_number
```

The `super()` function calls the parent constructor to initialize the bank information.

**Key learning:** Inheritance allows a child class to reuse existing functionality and add new attributes and methods.

**Privacy note:** Use fictional identification numbers in practice examples. Never publish real PAN or Aadhaar numbers in a public repository.

### 11. Method Overloading

Method overloading traditionally means defining multiple methods with the same name but different parameter lists.

Python does not support traditional method overloading by defining several methods with the same name in one class. When methods are redefined, the latest definition replaces the earlier one.

Your `Information` examples demonstrate this behavior.

For example:

```python
class Information:
    def data(self, x):
        print(x)

    def data(self, x, y):
        print(x, y)

    def data(self, x, y, z):
        print(x, y, z)
```

Only the last `data()` definition remains available.

To support different numbers of arguments, Python provides alternatives.

#### A. Default Parameters

```python
class Information:
    def data(self, x=0, y=0, z=0):
        print(x, y, z)
```

This method can be called with zero, one, two, or three arguments.

#### B. Variable Positional Arguments (`*args`)

```python
class Information:
    def data(self, *args):
        print(args)
```

This allows the method to accept any number of positional arguments.

#### C. Variable Keyword Arguments (`**kwargs`)

```python
class Information:
    def data(self, **kwargs):
        print(kwargs)
```

This allows the method to accept any number of keyword arguments.

**Key learning:** Default parameters, `*args`, and `**kwargs` provide flexible ways to handle varying inputs in Python.

### 12. Constructor Overloading

Constructor overloading refers to using different constructor signatures to initialize objects in different ways.

Python does not support traditional constructor overloading by retaining multiple `__init__()` definitions in the same class.

In your example, the class defines `__init__()` three times. Only the last definition is retained.

```python
class Dim:
    def __init__(self, a=None, b=None):
        print("constructor3")

d = Dim(10)
```

**Output:**

```text
constructor3
```

The last constructor accepts optional parameters, so the object can be created with one argument or with no arguments.

---

## 🛠️ Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

## ▶️ How to Run

1. Install Python 3.
2. Copy an example into a Python file.
3. Save the file as `python_polymorphism.py`.
4. Open a terminal in the file's directory.
5. Run the following command:

```bash
python python_polymorphism.py
```

**Important:** Most examples in the original code are enclosed in triple quotes. Remove those quotes from the example you want to execute.

The active code includes the duck-typing loop, `AllOperation` class, and bank inheritance example.

## 📚 Learning Outcomes

After completing this project, you should understand:

* How duck typing enables flexible object behavior.
* How polymorphism allows different objects to respond to the same method call.
* How magic methods customize operator behavior.
* How to overload arithmetic and comparison operators.
* How `__str__()` and `__repr__()` affect object representation.
* How inheritance and `super()` work.
* Why Python does not support traditional method and constructor overloading.
* How default parameters, `*args`, and `**kwargs` provide flexible method signatures.

## 👨‍💻 Author

**Pranay Jadhao**

Learning Python, Object-Oriented Programming, and software development.

