import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('classic')

data = pd.read_csv('mouse_cod.csv')

x = data ['x']
y = data ['y']
plt.scatter(x,y,s=5,alpha=1, edgecolor='black',antialiased=False)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()


