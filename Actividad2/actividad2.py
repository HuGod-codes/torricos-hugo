import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class regressionLineal():
    def __init__(self, tipoDeDatos, N):
        self.tipoDeDatos = tipoDeDatos
        self.tamano = N

    def visualizar(self, y, x, num):

        plt.figure(figsize=[8,6])
        plt.title("Scatter Plot")
        plt.xlabel("Variable Independiente X")
        plt.ylabel("Variable Dependiente Y")
        plt.scatter(x[:num], y[:num], c= '#008080', alpha= 0.5)

        option = int(input("(1) Para visualizar; (2) Para Guardar: "))
        if option == 1:
            plt.show()
        elif option == 2:
            plt.savefig("imagen1.jpg")
    
    def optimizar(self, y, x):
        xNew = x.reshape((-1,1))
        modelo = LinearRegression()
        modelo.fit(xNew, y)
        return (modelo.intercept_, modelo.coef_)
    
    def resultado(self, x, y, m, b):
        plt.figure()
        plt.scatter(x, y, marker = '.')
        x2 = np.linspace(0, 3, 1000)
        y2 = m*x2 + b
        plt.plot(x2, y2, c= '#ff0000')
        plt.show()

N = 1000

r = regressionLineal("simulado/real", N)

# variable independiente x
x = np.random.uniform(0.0, 3.0, N)

# variable dependiente y
error = np.random.uniform(2.0, 4.0, N)
y = 5 + 2*x + error

num = int(input("Numero de datos a visualizar: "))
r.visualizar(y, x, num)

b, m = r.optimizar(y, x)
r.resultado(x, y, m, b)