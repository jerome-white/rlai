import sys

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(sys.stdin)

sns.lineplot(x='step',
             y='episode',
             hue='experiment',
             data=df)

plt.grid(True)
plt.savefig('example-6.11.png')
