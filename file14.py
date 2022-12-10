file1=open('people1.txt',"r")
data = file1.read()
file1=open('people2.txt',"r") 
data2 = file1.read()
file=open ('file3.txt', 'w')
file.write(data)

