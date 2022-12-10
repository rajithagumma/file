fr=open("month.txt","r")
lines=fr.readlines()
ptr=1
fw=open("month.txt","w")
for line in lines:
          if ptr!=5:
                    fw.write(line)
          ptr+=1
print("deleted")