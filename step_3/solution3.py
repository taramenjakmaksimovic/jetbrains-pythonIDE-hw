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

    sb.set_theme()
    fig=plt.figure(figsize=(14, 8))
    fig.canvas.manager.set_window_title('Game Platform Analysis')
    plot = sb.barplot(x='platform', y='count', hue='genre', data=count_data, 
                      order=platforms, hue_order=genre_order) 
    
    legend=plt.legend(title='genre', loc= 'center right', bbox_to_anchor=(1.14, 0.5))
    frame = legend.get_frame()
    frame.set_facecolor('white')
    frame.set_edgecolor('white')


    

    
    plt.show()

    return plot
