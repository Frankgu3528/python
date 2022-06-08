from matplotlib.font_manager import FontProperties
import numpy as np
import random 
import matplotlib.pyplot as plt
plt.style.use("seaborn")
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
print('请输入角色初始暴击率')
print('请输入角色暴击伤害')
a=float(input())    #读入初始暴击率
b=float(input())    #读入初始暴击伤害
print('下面开始计算~')
m=a
baojilv=[]
cishu=[]
shanghai=[]
baop=[]
shangp=[]
for i in range(300):
    r=random.random()
    if r > a:       #如果某次平a没有暴击
        a=a+0.08    #下一次暴击率提高8%
    else:
        a=m         #如果没有暴击，则移除专注效果   
    if a>=m+0.40:   #专注效果最多叠加4次
        a=m+0.40
    a=round(a,2)    #小数保留两位
    x=1+a*b
    baojilv.append(a) 
    cishu.append(i)
    shanghai.append(x)
    k=np.average(shanghai)
    s=np.average(baojilv)
    baop.append(s)
    shangp.append(k)
#数据可视化
plt.xlabel("试验次数",) 
plt.ylabel("暴击率/伤害")
plt.title("宗室剑的伤害模拟（按初始5%爆率计算）")
plt.plot(cishu,baojilv,label="暴击率")
plt.plot(cishu,shanghai,label="理论伤害")
plt.plot(cishu,baop,label="暴击率期望")
plt.plot(cishu,shangp,label="伤害期望")
plt.legend()
plt.show()

