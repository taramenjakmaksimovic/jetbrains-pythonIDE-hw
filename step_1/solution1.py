import os
import pandas as pd


def load_data(dataset):
    filepath = os.path.join('..', dataset)
    data_csv = pd.read_csv(filepath)
    return data_csv


def filter_and_group(data_csv):
    platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    filtered_data = data_csv[data_csv['platform'].isin(platforms)]
    count_data = filtered_data.groupby(['platform', 'genre']).size().reset_index(name='count')
    return count_data
