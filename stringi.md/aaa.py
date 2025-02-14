teikums = input()
vardi = teikums.split()
for vards in vardi:
    lielo_sk=0
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            lielo_sk+=1
    print(lielo_sk, end=" ")