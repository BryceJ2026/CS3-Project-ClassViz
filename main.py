import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Set style theme
plt.style.use('seaborn-v0_8-pastel')

# Read CSV into DataFrame
df = pd.read_csv('classdatav1.csv')
print(df.info())
colors = ['yellow', 'green']

# NOTE: some columns need data type converted (object -> boolean)
plt.pie(df['Wisdom Teeth Removed'].dropna(), startangle=270)

plt.title('Wise vs Wisdom Teeth Removed')
plt.savefig('wisebar.png', bbox_inches='tight')