import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

platforms=['PS4', 'XOne', 'PC', 'WiiU']
data_csv=pd.read_csv('../dataset.csv')
filtered_data = data_csv[data_csv['platform'].isin(platforms)]
count_data = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='count')
genre_order = ['Action', 'Adventure', 'Fighting', 'Misc', 'Platform', 'Puzzle', 'Racing', 'Role-Playing', 
               'Shooter', 'Simulation', 'Sports', 'Strategy' ]
#print(count_data) this is for the purpose of testing, see test2.py
plot=sb.barplot(x='platform', y='count', hue='genre', data=count_data, 
            order=platforms, hue_order=genre_order)
plt.show()