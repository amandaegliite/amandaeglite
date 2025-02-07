pirmais = input()
otrais = input()
sakrita = 0
for p in range(len(pirmais)):
    for o in range(len(otrais)):
        if pirmais[p]==otrais[o]:
            sakrita+=1
            otrais = otrais[:o]+'#'+otrais[o+1:]
            break
if sakrita==len(otrais):

print("VAR")

else:

print("NEVAR")
