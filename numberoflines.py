file=open("question3.txt","r")
c=0
a=file.read()
b=a.split("\n")
i=0
while i<len(b):
    k=b[i]
    r=k.split("-")
    j=0
    while j<len(r):
        if type(r[j])==str:
            c=c+1
        j=j+1
    i=i+1
print("number of lines is",i)
print("number of words in a file is",c)

fp=open("question3.txt","a")
print("number of all characters is ",fp.tell()) 
        
file.close()

