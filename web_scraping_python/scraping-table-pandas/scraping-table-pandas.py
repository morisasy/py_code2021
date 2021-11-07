# pip install pandas

import pandas as pd

url = 'https://fastestlaps.com/tracks/le-mans-bugatti'
# url = 'https://en.wikipedia.org/wiki/land_speed_record'

df = pd.read_html(url)
print(df)
print('')
print('display main table')
#print(df[0].head(15))
df[0].to_csv('fastestlaps.csv')
