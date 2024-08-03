# MatPlotLib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from icecream import ic

characters_og = pd.read_csv('characters_stats.csv')
characters = characters_og.copy()
ic(characters.head())

ic(characters['Alignment'].value_counts())

# get all the good people
good = characters[characters['Alignment']=='good']
ic(good.head())

# get the people whos speed is 100

max_speed_good = good[good['Speed']==100]
ic(max_speed_good)


#get the people whos speed is 1

min_speed_good = good[good['Speed'] == 1]
ic(min_speed_good)

# sort good people by power
good_sorted_power = good.sort_values(by='Power', ascending=False)
ic(good_sorted_power)

#find the good guys with the maximum power
good_max_stats = good.sort_values(by='Total',ascending=False)
ic(good_max_stats)

#sort the good guys with the most intelligence
good_intelligence = good.sort_values(by='Intelligence',ascending=False)
ic(good_intelligence)

plt.bar(list(good_max_stats['Name'])[0:5],list(good_max_stats['Total'])[0:5])
# plt.show()
plt.clf()

plt.bar(list(good_intelligence['Name'])[0:5],list(good_intelligence['Intelligence'])[0:5],color='g')
# plt.show()
plt.clf()
characters = characters_og.copy()
bad = characters[characters['Alignment']=='bad']

ic(bad.head())
pd.options.display.max_columns = None

bad_speed= bad.sort_values(by='Speed',ascending=False)
ic(bad_speed.head())

bad_max_speed = bad[bad['Speed']==100]
ic(bad_max_speed.head())

bad_min_speed = bad[bad['Speed']==1]
ic(bad_min_speed.head())

strongest_bad = bad.sort_values(by='Total',ascending=False)
ic(strongest_bad)

plt.bar(list(strongest_bad['Name'])[0:5],list(strongest_bad['Total'])[0:5],color='r')
# plt.show()
plt.clf()

plt.hist(list(good['Speed']),bins=50)
plt.title('Distribution of Speed')
plt.xlabel('Speed')
plt.show()
