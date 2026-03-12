import pandas as pd
import numpy as np 

df = pd.read_csv('petr4.csv')
df['retorno_log'] = np.log(df['price']/df['price'].shift(1))
print(df.head())
