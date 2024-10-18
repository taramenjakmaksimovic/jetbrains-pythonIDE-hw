# Theory 📖

## Seaborn introduction 📊
[Seaborn](https://seaborn.pydata.org/) is a Python visualization  library that is based on another visualization library, matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

To perform statistical analysis, we require data, which is typically not entered manually in programs. Common methods for storing data include tabular formats, databases, and text files. 
For this lesson we are going to use a CSV file, which is a type of text file. Seaborn libary doesn't have a feature or functionality for reading data, so instead we are going to use another Python library, [Pandas](https://pandas.pydata.org/). Pandas functionality for reading a CSV file is `data_name=pd.read_csv('filename.csv')`, where pd is an alias for pandas. 

> **Note**
>
>  To load a file that is in the parent directory: `data_name = pd.read_csv('../filename.csv')`. <br>
>  To load a file that is in the child directory: `data_name=pd.read_csv('child_directory/filename.csv')`.
>

# Task 🤓
Load the CSV file provided (which is in the parent directory), filter data only for platforms PS4, XOne, PC and WiiU. After that, group the data by platform and genre, and count the entries by each combination. 

