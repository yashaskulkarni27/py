import pandas as pd

# Creating a Series
data_series = pd.Series([10, 20, 30, 40, 50], index=['A', 'B', 'C', 'D', 'E'])
print("Data Series:")
print(data_series)
print()

# Creating a DataFrame
data = {'Name': ['John', 'Jane', 'Bob', 'Alice', 'Eve'],
        'Age': [30, 25, 35, 28, 32],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami']}

data_frame = pd.DataFrame(data)
print("Data Frame:")
print(data_frame)
