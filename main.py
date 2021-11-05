import numpy as np
import matplotlib.pyplot as mlp

A = float(input("Enter Amplifier: "))
L = float(input("Enter Wave Frequenz: "))
x = np.arange(0, 10, 0.1)
print(x)

try:
    y = A*np.cos((2*np.pi/2)*x)
    print(y)
except:
    print("Calculation failed. Please Enter vaild Arguments")

mlp.plot(x, y)
mlp.show()