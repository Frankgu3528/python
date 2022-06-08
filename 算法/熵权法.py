from bleach import clean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel(io=r'C:\Users\阿漆\Desktop\data_shiyan.xlsx',sheet_name="广州")
df.drop(columns="时间",axis=1,inplace=True)
df.set_index([[2010,2011,2012,2013,2014,2015,2016,2017,2018]],inplace=True)
# 开始数据规范化
for i in list(df.columns):
    Max=np.max(df[i])
    Min=np.min(df[i])
    if (i=="二氧化氮年平均浓度") or (i=="二氧化硫年平均浓度"):
        df[i]=(Max-df[i])/(Max-Min)
    else:
        df[i]=(df[i]-Min)/(Max-Min)
print(df)
#计算指标比重
def bizhong(df_bizhong):
    for column in df_bizhong.columns:
        sigma_xij =sum(df_bizhong[column])
        df_bizhong[column] = df_bizhong[column].apply(lambda x_ij: x_ij / sigma_xij if x_ij / sigma_xij != 0 else 1e-6)
        #取1e-6是使接下来取对数的时候不至于无穷大
    return df_bizhong
df_bizhong=bizhong(df)
#算信息熵
k=1/np.log2(9)
e_j=(-k)*np.array([sum([pij*np.log2(pij) for pij in df_bizhong[column]]) for column in df_bizhong.columns])
#print(e_j)
#计算每个指标的权重(应该是权重*标准化后的数据)
s=sum(1-e_j)
w_j=np.array((1-e_j)/s)
#开始对每年的成果打分
w_j=w_j.T
F=np.dot(df,w_j)
#映射到100分制
m=F/sum(F)*100
print(m)
#可视化
x=np.array([2010,2011,2012,2013,2014,2015,2016,2017,2018])
plt.plot(x,m)
plt.show()