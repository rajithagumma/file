num=0
file=open("sample_file.txt","r")
data=file.read()
lines=data.split()
for word in lines:
          if not word.isnumeric():
                    num+=1
print(num)