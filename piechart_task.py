import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:\Downloads\Data.csv') # Path of your CSV file
new_df = df.groupby('Country').sum()
# print(df)
print(new_df)


death = [new_df['Death'][0], new_df['Death'][1], new_df['Death'][2]]
labels = ['Bangladesh', 'India', 'Pakistan']
plt.pie(death, labels=labels)
plt.show()
