import pandas as pd

df = pd.read_csv('petr4.csv')
df['retorno_simples'] = df['price'].pct_change()  
print(df.head())
