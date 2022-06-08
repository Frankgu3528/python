a=int(input())
if a<0 :
    print("Invalid Value!")
elif 0<=a<=50 :
    str="cost = %.2f"%(a*0.53)
    print(str)
elif a>50:
    str="cost = %.2f"%(50*0.53+(a-50)*0.58)
    print(str)
