liello_sk=0
teikums = input()
for i in range(len(teikums)):
    if teikums[i]>='A' amd teikums[i] <='Z':
       lielo_sk+=1
if lielo_sk>0:
    print("IR DRUKATIE")
else:
    print("NAV DRUKATIE")
    