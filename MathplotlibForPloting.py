import matplotlib.pyplot as plt
import numpy as np


x=[1,2,3,4,5]
y=[10,20,25,35,15]


plt.plot(x,y , color='red', linewidth=2, linestyle='--')


plt.title('Graph')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()