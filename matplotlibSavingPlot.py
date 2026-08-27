import matplotlib.pyplot as plt
import numpy as np


x=np.linspace(0,10,100)
y=np.sin(x)
plt.figure(figsize=(8,4))
plt.style.use('_mpl-gallery')
plt.plot(x,y,label="Sine Wave")

plt.title('Sine Wave Plot')
plt.savefig('Myplot.png')
plt.show()