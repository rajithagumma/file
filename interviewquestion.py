file=open("interview.txt","w")
first_f=open("dellhi.txt","r")
second_s=open("shimla.txt","r")
a=first_f.read()
b=second_s.read()
c=a.split("\n")
d=b.split("\n")
i=0
while i<len(c):
    file.write(c[i]+"\n")
    file.write(d[i]+"\n")
    i=i+1
file=open("interview.txt","r")
print(file.read())