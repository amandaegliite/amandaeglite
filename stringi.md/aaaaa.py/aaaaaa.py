teikums = input()
vardi=teikums.split()

for vards in vardi:
  abc =0

   for i in range (len(vards)-1):
      if vards[i]<vards[i+1]:
          abc +=1
           if abc==len(vards)-1:
   
  
   print("IR")
else:
   print("NAV")