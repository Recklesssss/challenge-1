import pandas as pd
import os

file_path1 = os.path.join('..', 'data', 'benin-malanville.csv')
file_path2 = os.path.join('..', 'data', 'sierraleone-bumbuna.csv')
file_path3 = os.path.join('..', 'data', 'togo-dapaong_qc.csv')

df1 = pd.read_csv(file_path1, parse_dates=['Timestamp'])
df2 = pd.read_csv(file_path2, parse_dates=['Timestamp'])
df3 = pd.read_csv(file_path3, parse_dates=['Timestamp'])

df = pd.concat([df1, df2, df3], ignore_index=True)
df.info()  

summary_stats = df.describe()
print(summary_stats)

missing_values = df.isnull().sum()
print(missing_values)

df.fillna(method='ffill', inplace=True)
