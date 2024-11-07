import numpy as np
import matplotlib.pyplot as plt

N = 1000

class regressionLineal():
    def __init__(self, a):
        self.nombre = a
    def visualize(self, y, x, num):
        option = int(input("(1) Para visulaizar; (2) Para Guardar"))
        if option == 1:
            print("ver imagen")
        elif option == 2:
            print("guardar imagen")

# variable independiente x
x = np.random.uniform(0.0, 3.0, N)

# variable dependiente y
b = np.random.uniform(2.0, 4.0, N)
y = 5 + 2*x + b

plt.figure(figsize=[8,6])
plt.title("Scatter Plot")
plt.xlabel("Variable Independiente X")
plt.ylabel("Variable Dependiente Y")
plt.scatter(x, y, marker = ".")
plt.show()