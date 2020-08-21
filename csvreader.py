import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import *

df = pd.read_csv('.\shenzhen.csv')
df = pd.DataFrame(df)
df.columns =['area','region','price']
print(df[['area','region','price']])
s = df.sort_values(by='price',ascending=False)
j = df.sort_values(by='price',ascending=True)
print(j)
print(s)
col_mean = df['price'].mean()
print(col_mean)
aa = s.iloc[:5,]
bb = j.iloc[:5,]
print(aa)

print('房屋单价最高为：',df['price'].max())
print('房屋单价最低为：',df['price'].min())
print('房屋单价均值为：',df['price'].mean())
fig,ax = plt.subplots()
ax.boxplot(df['price'])
plt.show()


fig,ax = plt.subplots()
ax.bar(aa['area'],aa['price'],color='orange')
mpl.rcParams['font.sans-serif']=['SimHei']
plt.tick_params(labelsize=6)
plt.xticks(rotation=60)
for a,b in zip(aa['area'],aa['price']):
    plt.text(a, b, '%d' % b, ha='center', va= 'bottom',fontsize=5)
plt.ylabel('价格（元/平）')
plt.title('Top 20 of the most expensive unit price ')
plt.show()



fig,ax = plt.subplots()
ax.bar(aa['area'],aa['price'])
mpl.rcParams['font.sans-serif']=['SimHei']
plt.tick_params(labelsize=6)
for a,b in zip(aa['area'],aa['price']):
    plt.text(a, b, '%.1f' % b, ha='center', va= 'bottom',fontsize=9)
plt.ylabel('价格（元/平）')
plt.title('Top 5 of the most expensive unit price ')
plt.show()


fig,ax = plt.subplots()
ax.bar(bb['area'],bb['price'])
mpl.rcParams['font.sans-serif']=['SimHei']
plt.tick_params(labelsize=6)
for a,b in zip(bb['area'],bb['price']):
    plt.text(a, b, '%.1f' % b, ha='center', va= 'bottom',fontsize=9)
plt.ylabel('价格（元/平）')
plt.title('Top 5 of the cheapest unit price')
plt.show()


cc_200 = s.iloc[:100,]
print(cc_200)
count = cc_200['region'].value_counts()
print(count)

dd_200 = j.iloc[:100,]
print(dd_200)
count_dd = dd_200['region'].value_counts()
print(count_dd)


labels = ['宝安','龙华','布吉','光明','龙岗','福田','深圳周边','坪山', '南山','罗湖']
mpl.rcParams['font.sans-serif']=['SimHei']
plt.pie(count_dd,labels=labels,autopct='%1.1f%%')
plt.show()

labels = [ '南山','福田','宝安','罗湖','盐田']
mpl.rcParams['font.sans-serif']=['SimHei']
plt.pie(count,labels=labels,autopct='%1.1f%%')
plt.show()
