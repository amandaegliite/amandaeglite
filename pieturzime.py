lielo_sk=0
burtu_sk=0
teikums = input()
for i in range(len(teikums)):
    if teikums[i]>='A' and teikums[i] <='Z':
       lielo_sk+=1
if lielo_sk>0:
    print("IR DRUKATIE")
else:
    print("NAV DRUKATIE")

