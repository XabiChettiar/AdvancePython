import seaborn as sns
import matplotlib.pyplot as plt


df=sns.load_dataset('tips')

print(df)

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()