teikums = input()

vardi = teikums.split()

for vards in vardi :
  tris_simboli=0
for i in range (len(vards)):
   tris_simboli+=1

if tris_simboli == 3:
 print("1. IR 3 SIMBOLI")
else:
  print("1. NAV 3 SIMBOLI")

for vards in vardi :
  tris_simboli=0
  for i in range (len(vards)):
   tris_simboli+=1
if tris_simboli == 3:
  print("2." , vards)
else:
  print("2. NAV TADU VARDU")

vards_nr=0
for vards in vardi:
    vards_nr+=1
    if len(vards)%2==0:
      print("3.", vards_nr)
    
tas_pats = 0
for vards in vardi:
  if vards[0] == vards[-1]:
    tas_pats+=1
    print("4.")
    print(tas_pats)
