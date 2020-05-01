import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('[sharewood.band] correlation.tsv', sep='\t')
data.drop('month', axis=1, inplace=True)
data.corr() #делаем корреляцию
f, ax = plt.subplots(figsize=(15, 10)) #устанавливаем размеры области
sns.heatmap(data.corr(), annot=True, fmt='.1f', ax=ax, cmap=sns.color_palette('coolwarm', 16)) #хитмап


