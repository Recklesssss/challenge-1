import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import zscore

file_path1 = os.path.join('..', 'data', 'benin-malanville.csv')
file_path2 = os.path.join('..', 'data', 'sierraleone-bumbuna.csv')
file_path3 = os.path.join('..', 'data', 'togo-dapaong_qc.csv')

df1 = pd.read_csv(file_path1, parse_dates=['Timestamp'])
df2 = pd.read_csv(file_path2, parse_dates=['Timestamp'])
df3 = pd.read_csv(file_path3, parse_dates=['Timestamp'])

df = pd.concat([df1, df2, df3], ignore_index=True)


# Time Series Analysis
df.set_index('Timestamp')[['GHI', 'DNI', 'DHI', 'Tamb']].plot(subplots=True)
plt.show()

# Correlation Analysis
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()

# Wind Analysis
df['WD_rad'] = np.deg2rad(df['WD'])
ax = plt.subplot(projection='polar')
ax.scatter(df['WD_rad'], df['WS'])
plt.show()

# Histograms and Z-Score Analysis
df['GHI_zscore'] = zscore(df['GHI'])
df[['GHI', 'GHI_zscore']].hist()
plt.show()
