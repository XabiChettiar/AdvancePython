import matplotlib.pyplot as plt
import numpy as np


days=np.arange(1,11)
sales_in_cr=np.array([2.5,3.0,4.2,5.1,6.0,7.8,8.5,9.0,10.2,11.5])         

plt.figure(figsize=(10,5))
plt.plot(days,sales_in_cr, marker='o')
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('Sales in cr')
plt.show()