file=open("question3.txt","r")
delhi=open("dellhi.txt","w")
shimla=open("shimla.txt","w")
other=open("others.txt","w")
a=file.read()
b=a.split('\n')
for place in b:
          if "delhi" in place:
                    delhi.write(place+"\n")
          elif "shimla" in place:
                    shimla.write(place+"\n")
          else:
                    other.write(place+"\n")
print(a)