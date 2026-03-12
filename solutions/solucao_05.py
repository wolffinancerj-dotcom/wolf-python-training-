import pandas as pd
import numpy as np 

df = pd.read_csv('btc.csv')

print(df['Volume'].std())
