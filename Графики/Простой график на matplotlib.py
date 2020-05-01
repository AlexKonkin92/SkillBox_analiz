import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('[sharewood.band] sales_data.csv', sep=';')
plt.title("Продажи за 3 года по месяцам")
plt.plot(data['month'], data['2016'], marker='o') # x и y 
plt.plot(data['2017'], linestyle='dashed') # ось y
plt.plot(data['2018'], linewidth=3) # ось y
plt.legend()




