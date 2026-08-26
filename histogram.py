import matplotlib.pyplot as plt
import numpy as np


data=np.random.randn(1000)

print(data)


plt.hist(data,bins=3, edgecolor='black')    

plt.show()