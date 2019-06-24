#22920172204299-赵筱萱-py数据分析

import pandas as pd
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
from IPython.display import display 
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] 
# 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False 
# 解决保存图像是负号'-'显示为方块的问题

sheet_names = ["思明区","湖里区","海沧区","集美区","同安区", "翔安区"]
df = None
for sheet_name in sheet_names:
	_df = pd.read_excel('data.xls', usecols=[1,2,3,4,5,6,7,8,9],sheet_name=sheet_name)
	if df is None:
		df = _df
	else:
		df = pd.concat([df, _df], ignore_index=True)

def data_adj(area_data, str):#判断‘str’在不在这个数据里
	if str in area_data :#用find()函数查找字符串的索引位置，方便截取        
		return int(area_data[0 : area_data.find(str)])
	else :
		return None#去掉单价的单位

df['单价'] = df['单价'].apply(data_adj,str = '元')
df['建造年份'] = df['建造年份'].apply(data_adj,str = '年建造')
df['面积'] = df['面积'].apply(data_adj,str = 'm')

display(df.describe())#显示各统计量最大最小中位数等等
price = df['单价']
max_price = price.max()#最大单价
min_price = price.min()#最小单价
mean_price = price.mean()#单价平均数
median_price = price.median()#单价中位数
#存储以便后面使用

"""#最贵的5套房
df['标题']
df[['总价','标题']]
df[df['总价']<100][['总价','标题']]

top5_all=df.sort_values('总价',ascending=False).head(5)
top5=df.sort_values('总价',ascending=False).head(5)[['总价','标题']]
print(top5)
"""#最贵的5套房

"""#面积分布
housetype = df['户型'].value_counts()
plt.figure()
housetype.head(10).plot(kind='bar',  title='户型数量分布图')
plt.legend(['数量'])
plt.show()

housetype = df['面积'].value_counts()
plt.figure()
housetype.head(10).plot(kind='bar',  title='面积分布图')
plt.xlable(['平方米'])
plt.ylable(['数量'])
plt.legend(['面积'])
plt.show()
"""#面积分布

"""#户型分布
housetype = df['户型'].value_counts()
#print(housetype)
#plt.figure()
housetype = housetype.head(10).plot(kind='bar',  title='户型数量分布图')
#plt.legend(['数量'])
#plt.show()
f, ax1= plt.subplots(figsize=(20,20)) 
sns.countplot(y='户型', data=housetype, ax=ax1) 
ax1.set_title('房屋户型',fontsize=15) 
ax1.set_xlabel('数量') 
ax1.set_ylabel('户型') 
plt.show() 
"""#户型分布

"""#二手房价格直方图
plt.xlim(0,150000)
plt.ylim(0,1000)
plt.title("厦门市二手房价格分析")
plt.xlabel("二手房价格 (元/平方米)")
plt.ylabel("二手房数量")
plt.hist(price, bins=200)
plt.vlines(mean_price, 0, 500, color='red',label='平均价格', linewidth=1.5, linestyle='--')
plt.vlines(median_price, 0, 500, color='red',label='中位数价格', linewidth=1.5)
plt.legend()
plt.show()
"""#二手房价格直方图

"""#面积-价格
f, [ax1,ax2] = plt.subplots(1, 2, figsize=(15, 5)) 
# 面积的分布情况 
sns.distplot(df['面积'], bins=20, ax=ax1, color='r') 
sns.kdeplot(df['面积'], shade=True, ax=ax1) 
# 面积和出售价格的关系 
sns.regplot(x='面积', y='单价', data=df, ax=ax2) 
plt.show() 
"""#面积-价格

"""#建造年份-价格
f, [ax1,ax2] = plt.subplots(1, 2, figsize=(15, 5)) 
# 建造年份的分布情况 
sns.distplot(df['建造年份'], bins=20, ax=ax1, color='r') 
sns.kdeplot(df['建造年份'], shade=True, ax=ax1) 
# 建造年份和出售价格的关系 
sns.regplot(x='建造年份', y='单价', data=df, ax=ax2) 
plt.show() 
"""#建造年份-价格

"""#各区单价对比折线图
plt.figure(figsize=(6,4),dpi=200)
district = ["同安区","思明区","海沧区","湖里区", "翔安区","集美区"]
region1=df.groupby('区域').max()['单价']#将总价改为代为单价即可得到关于单价的折线关系图
region2=df.groupby('区域').min()['单价']
region3=df.groupby('区域').mean()['单价']
region4=df.groupby('区域').median()['单价']
x=district
plt.plot(x,region1,color='b',label='最高')
plt.plot(x,region2,color='r',label='最低')
plt.plot(x,region3,color='m',label='均价')
plt.plot(x,region4,color='y',label='中位价')
plt.legend(loc=1,bbox_to_anchor=(1.0,1.0),fontsize=12)
plt.title("厦门市各行政区二手房关于单价的情况分析(折线图)")
plt.show()
"""#各区单价对比折线图

"""#区域分组对比二手房每平米房价 
df_house_count = df.groupby('区域')['总价'].count().sort_values(ascending=False).to_frame().reset_index() 
df_house_mean = df.groupby('区域')['单价'].mean().sort_values(ascending=False).to_frame().reset_index() 
 
f, ax1 = plt.subplots(1,1,figsize=(20,15))
sns.barplot(x='区域', y='单价', palette="Blues_d", data=df_house_mean, ax=ax1) 
ax1.set_title('厦门各区二手房每平米单价对比',fontsize=15) 
ax1.set_xlabel('区域') 
ax1.set_ylabel('每平米单价') 
plt.show()
"""#区域分组对比二手房每平米房价
 
"""#各区总价对比箱型图
f, ax3 = plt.subplots(1,1,figsize=(20,15))
sns.boxplot(x='区域', y='总价', data=df, ax=ax3) 
ax3.set_title('厦门各大区二手房房屋总价',fontsize=15) 
ax3.set_xlabel('区域') 
ax3.set_ylabel('房屋总价') 
plt.show() 
"""#各区总价对比箱型图

"""#各区建造年份对比箱型图
f, ax3 = plt.subplots(1,1,figsize=(20,15))
sns.boxplot(x='区域', y='建造年份', data=df, ax=ax3) 
ax3.set_title('厦门各大区二手房房屋年份',fontsize=15) 
ax3.set_xlabel('区域') 
ax3.set_ylabel('建造年份') 
plt.show() 
"""#各区建造年份对比箱型图

"""#各区单价对比箱型图
f, ax3 = plt.subplots(1,1,figsize=(20,15))
sns.boxplot(x='区域', y='单价', data=df, ax=ax3) 
ax3.set_title('厦门各大区二手房房屋单价',fontsize=15) 
ax3.set_xlabel('区域') 
ax3.set_ylabel('单价') 
plt.show() 
"""#各区单价对比箱型图

"""#分区面积
f, ax1 = plt.subplots(1,1,figsize=(20,15))
colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']
district = ["思明区","湖里区","海沧区","集美区","同安区", "翔安区"]
markers = ['o','s','v','x','*', '.']
for i in range(6):
    x = df.loc[df['区域'] == district[i]]['面积']
    y = df.loc[df['区域'] == district[i]]['总价']
    ax1.scatter(x, y, c=colors[i], label=district[i], marker=markers[i])
ax1.legend(loc=1,bbox_to_anchor=(1.0,1.0))
ax1.axis([0,600,0,5000])

ax1.set_title('厦门各行政区面积对房屋总价的影响（散点图）')
ax1.set_xlabel('面积（平方米）')
ax1.set_xlabel('房屋总价（万元）')
plt.show()
"""

"""#分区年代
f, ax1 = plt.subplots(1,1,figsize=(20,15))
colors = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow']
district = ["思明区","湖里区","海沧区","集美区","同安区", "翔安区"]
markers = ['o','s','v','x','*', '.']
for i in range(6):
    x = df.loc[df['区域'] == district[i]]['建筑年代']
    y = df.loc[df['区域'] == district[i]]['总价']
    ax1.scatter(x, y, c=colors[i], label=district[i], marker=markers[i])
ax1.legend(loc=1,bbox_to_anchor=(1.0,1.0))
ax1.axis([1980,2018,0,10000])

ax1.set_title('厦门各行政区建筑年代对房屋总价的影响（散点图）')
ax1.set_xlabel('面积（平方米）')
ax1.set_xlabel('房屋总价（万元）')
plt.show()
"""
