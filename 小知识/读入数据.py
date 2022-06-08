#方法1（读入未知数量的正整数）
#list=list(map(int,input().split()))
#print(list)
#(第一行输入数据个数；后面每隔一行读入一个数据)
n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))