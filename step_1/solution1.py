import pandas as pd

platforms=['PS4', 'XOne', 'PC', 'WiiU']
data_csv=pd.read_csv('../dataset.csv')
filtered_data = data_csv[data_csv['platform'].isin(platforms)]
count_data = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='count')
