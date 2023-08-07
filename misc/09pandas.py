# pip install pandas

import pandas as pd

# series -> 1D
# data = [10,20,30,40,50]
# series = pd.Series(data)
# print(series)

# dataframes -> 2D
data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [25, 30, 35],
    'City': ['NY' , 'San Fransisco', 'Chicago']
}

df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('data.csv')
# print(df)

# Read Excel Files
# df = pd.read_excel('data.xlsx', sheet_name = 'Sheet1')
# print(df)


# display the first few rows of DataFrame
# print(df.head())
# print(df.describe())


# selected_data = df.loc[df['City'] == 'NY', ['Name', 'Age']]
# print(selected_data)

grouped_data = df.groupby('Name')['Age'].mean()
print(grouped_data)

