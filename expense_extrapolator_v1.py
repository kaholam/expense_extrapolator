import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('monthly_expenses.xlsx')

df['Date'][0]=1
df['Date'][1]=2
df['Date'][2]=3
df['Date'][3]=4
df['Date'][4]=5

x = np.array(df['Date'])
y = df['Expense']
plt.xlabel('Period')
plt.ylabel('Expense')
plt.plot(x,y,'o')
m,b = np.polyfit(list(x),y,1)
plt.plot(x,m*x + b)
print('Expense = {} + {} * Period'.format(b,m))
print('')
