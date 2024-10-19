import pandas as pd
import seaborn as sb
import os
import matplotlib.pyplot as plt

def load_data(dataset):
    filepath = os.path.join('..', dataset)
    data_csv = pd.read_csv(filepath)
    return data_csv

def create_barplot(data_csv, platforms, genre_order):
    filtered_data = data_csv[data_csv['platform'].isin(platforms)]
    count_data = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='count')
    
    plot = sb.barplot(x='platform', y='count', hue='genre', data=count_data, 
                      order=platforms, hue_order=genre_order)
    plt.show()
    return plot
