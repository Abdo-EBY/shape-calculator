# Shape Calculator 🧮

This project is part of the **Scientific Computing with Python** certification from [freeCodeCamp.org](https://www.freecodecamp.org/).

### 📌 Project Description

This is a simple Python program that defines a `Rectangle` and `Square` class to perform basic geometric operations such as:

- Calculating area, perimeter, and diagonal
- Representing the shape using ASCII art
- Getting string representations

### 🧪 How to Use

You can create and manipulate shapes like this:

```python
from shape_calculator import Rectangle, Square

rect = Rectangle(10, 5)
print(rect.get_area())       # Output: 50
print(rect.get_picture())    # Prints rectangle in stars

sq = Square(3)
print(sq.get_perimeter())    # Output: 12