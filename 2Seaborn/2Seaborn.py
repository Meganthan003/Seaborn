import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
a = sns.load_dataset('tips')

# Strip Plot
sns.stripplot(x='day', y='total_bill', data=a)
plt.title('Strip Plot of Total Bill by Day')
plt.savefig("Stripplot.png")
plt.show()

# Swarm Plot
sns.swarmplot(x='day', y='total_bill', data=a)
plt.title('Swarm Plot of Total Bill by Day')
plt.savefig("Swarmplot.png")
plt.show()

# Histogram
sns.histplot(x='total_bill', data=a)
plt.title('Histogram of Total Bill')
plt.savefig("Histogram.png")
plt.show()

# KDE Plot
sns.kdeplot(x='total_bill', data=a,fill=True,hue='sex')
plt.title('KDE Plot of Total Bill by Sex')
plt.savefig("KDEplot.png")  
plt.show()


#displot
sns.displot(x='total_bill', data=a, col='time',hue='sex')
plt.title('Displot of Total Bill by Time and Sex')
plt.savefig("Displot.png") 
plt.show()

#regplot
sns.regplot(x='total_bill', y='tip', data=a)
plt.title('Regression Plot of Tip vs Total Bill')
plt.savefig("Regressionplot.png")
plt.show()

#lmplot
sns.lmplot(x='total_bill', y='tip', data=a, hue='sex')
plt.title('Linear Model Plot of Tip vs Total Bill by Sex')
plt.savefig("LinearModelplot.png")
plt.show() 

#heatmap
b=a.corr(numeric_only=True)
sns.heatmap(b, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.savefig("Heatmap.png")  
plt.show()

# Pair Plot
c=sns.load_dataset('iris')
sns.pairplot(c, hue='species')
plt.title('Pair Plot of Iris Dataset by Species')   
plt.savefig("Pairplot.png")
plt.show() 

# Joint Plot
sns.jointplot(x='total_bill', y='tip', data=a,kind='hex')
plt.title('Joint Plot of Tip vs Total Bill')
plt.savefig("Jointplot.png")
plt.show()

sns.set_style('whitegrid') #this is used to set the style of the plot
sns.set_context('talk') #this is used to set the context of the plot
sns.set_palette('pastel') #this is used to set the color palette of the plot
d=sns.FacetGrid(a, col='sex', row='sex')
d.map(sns.scatterplot, 'total_bill', 'tip')
plt.title('Facet Grid of Tip vs Total Bill by Sex')
plt.savefig("Facetgrid.png")
plt.show()