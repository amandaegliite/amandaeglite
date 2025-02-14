teikums = input()
vardi = teikums.split()
for i in range (len(vardi)):
    lielo_sk=0
    for j in range(len(vardi[i])):
        if vardi[i][j]>='A' and vardi[i][j]<='Z':
            lielo_sk+=1
            if lielo_sk==len(vardi[i]):
              print(i+1, end=" ")