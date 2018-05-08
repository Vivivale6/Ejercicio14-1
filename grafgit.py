import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi)
y=[]
for i in x:
    y.append(np.sin(i))

plt.plot(x,y)
plt.savefig("graficagit.png")


ñ
