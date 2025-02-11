teikums = input()
a_sk=0
vardu_sk=1
pirmais_vards=""
garums=len(teikums)
print(garums)
pirmais_burts= teikums[0]
print(pirmais_burts)
pedejais_burts=teikums[-2]
print(pedejais_burts)
for i in range(len(teikums)):
    if teikums[i]=="a":
        a_sk+=1
        if teikums[i]=="A":
            a_sk+=1
print(a_sk)
for i in range(len(teikums)):
  if teikums[i]==" ":
     vardu_sk+=1
print(vardu_sk)
for i in range(len(teikums)):
   if teikums[i]==" ":
      breakelse: pirmais_vards=pirmais_vards+teikums[i]
      print(pirmais_vards)
      