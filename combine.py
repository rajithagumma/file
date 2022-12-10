filen=open("new.txt","w")
file1=open("dellhi.txt","r")
file2=open("shimla.txt","r")
file1lines=file1.readlines()
file2lines=file2.readlines()
for i in range(len(file1lines)):
          filen.write(file1lines[i]+"\n"+file2lines[i]+"\n")
filen=open("new.txt","r")
print(filen.read())