teikums.input()
garums=len(teikums)
saraksts = teikums.split()
print(saraksts)
burtu_saraksts=[]

for i in range(len(saraksts)):
    if(len(saraksts[i]))>5:
        burtu_saraksts.append(saraksts[i])


