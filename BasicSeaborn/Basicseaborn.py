import seaborn as sns
import matplotlib.pyplot as plt
'''
print(a.head())
'''
a=sns.load_dataset('tips')
sns.scatterplot(x='total_bill', y='tip', data=a,hue='sex',size='size')
plt.title('Scatter plot of Total Bill vs Tip')
plt.savefig('scatterplot.png')
plt.show()


b=sns.load_dataset('flights')
sns.lineplot(x='year', y='passengers', data=b)
plt.title('Line plot of Year vs Passengers')
plt.savefig('lineplot.png')
plt.show()

sns.relplot(x='total_bill', y='tip', data=a,hue='smoker')
plt.savefig('relplot.png')
plt.show()


sns.barplot(x='day', y='total_bill', data=a,hue='sex',errorbar=None)
plt.savefig('barplot.png')
plt.show()

sns.countplot(x='day', data=a,hue='sex')
plt.savefig('countplot.png')
plt.show()

sns.boxplot(x='day', y='total_bill', data=a ,hue='smoker')
plt.savefig('boxplot.png')
plt.show()

sns.violinplot(x='day', y='total_bill', data=a ,hue='sex',split=True)
plt.savefig('violinplot.png')
plt.show()
