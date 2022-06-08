n=int(input())
for number in range(n):
    m=int(input())  
    mat=[]
    for row in range(m):
        mat.append(input().split())
    lstupper=[int(mat[i][j]) for i in range(m) for j in range(m) if i<j]
    lstlower=[int(mat[i][j]) for i in range(m) for j in range(m) if i>j]
    if sum(lstlower)==0:
       print("upper triangular matrix")
    elif sum(lstupper)==0:
       print("lower triangular matrix")
    else:
       print("no")