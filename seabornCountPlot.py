import seaborn as sns
import matplotlib.pyplot as plt


df=sns.load_dataset('tips')

print(df)

sns.countplot(x='day', data=df)
plt.show()