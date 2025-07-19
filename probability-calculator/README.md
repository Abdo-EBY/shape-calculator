# 🎲 Probability Calculator

This is a Python project from the [freeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) certification.

It simulates drawing colored balls from a hat to estimate probabilities using random experiments.

---

## 📌 Project Overview

- Defines a `Hat` class to hold balls of different colors.
- Implements a `draw()` method to randomly extract balls.
- Includes an `experiment()` function to estimate the probability of drawing a specific set of balls after a number of draws.

---

## 🧪 Example Usage

```python
from prob_calculator import Hat, experiment

# Create a hat with colored balls
hat = Hat(red=3, blue=2)

# Run an experiment
probability = experiment(hat, {"red": 2}, 3, 1000)

print("Estimated Probability:", probability)