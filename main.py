import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Set style theme
plt.style.use('seaborn-v0_8-pastel')

# Read CSV into DataFrame
df = pd.read_csv('classdatav1.csv')
df = df.head(8)
print(df.info())
colors = ['yellow', 'green']

# NOTE: some columns need data type converted (object -> boolean)

df['Wise'] = pd.to_numeric(df['Wise']).fillna(0).astype(bool)
df['Wisdom Teeth Removed'] = pd.to_numeric(df['Wisdom Teeth Removed']).fillna(0).astype(bool)
teethe = df['Wisdom Teeth Removed'].value_counts()
plt.pie(teethe.values, labels=teethe.index, colors=colors, startangle=20)
plt.axis('equal')

plt.title('Wisdom Teeth Removed')
plt.legend()
plt.savefig('wisepie.png', bbox_inches='tight')
plt.close()


xthing = df['Best Water Swim'] # y values
ything = df['Flavor'] # x values
plt.scatter(ything, xthing, cmap='RdPu')

plt.savefig('scatter-flavorvision.png')
plt.close()

xstuff = df['BigFive Neuroticism']
ystuff = df['BigFive Agreeableness']
plt.title('Neuroticism vs Agreeableness')
plt.scatter(xstuff,ystuff)
plt.savefig('maybe.png')
plt.close()



df[''] = pd.to_numeric(df['Wise']).fillna(0).astype(bool)
df['Wisdom Teeth Removed'] = pd.to_numeric(df['Wisdom Teeth Removed']).fillna(0).astype(bool)
teethe = df['Wisdom Teeth Removed'].value_counts()
plt.pie(teethe.values, labels=teethe.index, colors=colors, startangle=20)
plt.axis('equal')

plt.title('Wisdom Teeth Removed')
plt.legend()
plt.savefig('wisepie.png', bbox_inches='tight')
plt.close()