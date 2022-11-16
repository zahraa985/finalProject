import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import numpy as np

headers = ['date','discharge']
data = pd.read_csv('hooverDailyDischarge.csv', delimiter='\t', names=headers)

ax = data.set_index('date').plot()

ax.get_legend().remove()
plt.title("Hoover Dam Mean Daily Discharge 9/13/2020-9/13/2021")
plt.xlabel("Date YYYY-MM-DD")
plt.xticks(rotation = 33)
plt.ylabel("Mean Daily Discharge cft/s")
plt.savefig('hooverDailyDishcharge2020-21.png', bbox_inches='tight')

print(np.shape(data))
