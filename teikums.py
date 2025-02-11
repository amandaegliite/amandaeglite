teikums = input("Jauka diena.:").strip()
simbolu_sk = len(teikums)
pirmais_burts = teikums[0]
pedejais_burts = teikums[-2]
 if teikums.endswith('.'):
    pedejais_burts = teikums[-2]
else:
    pedejais_burts = teikums[-1]
print(pedejais_burts)
a_sk = teikums.lower().count('a')
vardu_sk = len(teikums[:-1].split())
pirmais_vards = teikums.split()[0]



print(simbolu_sk)
print(pirmais_burts)

print(a_sk)
print(vardu_sk)
print(pirmais_vards)