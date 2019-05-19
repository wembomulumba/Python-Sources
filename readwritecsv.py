# Python Data Science Demo: Manipulating CSV downloaded from Internet
import datetime as dt      
import matplotlib.pyplot as plt  
from matplotlib import style   

import pandas as pd      
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2017,2,2)
end = dt.datetime(2018,12,31)

df = web.DataReader('TSLA', 'yahoo', start, end)



#print(df.head(4))
#df.to_csv('tsla.csv')

# to read a csv
df = pd.read_csv('tsla.csv')
print(df.head(6))

