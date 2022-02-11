magic_square=[[8,3,4],[1,5,9],[6,7,2]]
row1=0
row2=0
row3=0
coloumn1=0
coloumn2=0
coloumn3=0
diagonal1=0
diagonal2=0
i=0
while i<len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==0:
            row1+=magic_square[i][j]
        elif i==1:
            row2+=magic_square[i][j]
        elif i==2:
            row3+=magic_square[i][j]
        j=j+1
    i=i+1
a=0
while a<len(magic_square):
    k=0
    while k<len(magic_square[a]):
        if k==0:
            coloumn1+=magic_square[a][k]
        elif k==1:
            coloumn2+=magic_square[a][k]
        elif k==2:
            coloumn3+=magic_square[a][k]
        k=k+1
    a=a+1
b=0
while b<len(magic_square):
    s=0
    while s<len(magic_square[b]):
        if b==s:
            diagonal1+=magic_square[b][s]
        if b+s==len(magic_square[b])-1:
            diagonal2+=magic_square[b][s]
        s=s+1
    b=b+1
if row1==row2==row3==coloumn1==coloumn2==coloumn3==diagonal1==diagonal2:
    print(row1)
    print(coloumn1)
    print(diagonal1)
    print("it is magic squre")
else:
    print("it is not magic squre")