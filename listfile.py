# banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda\n"]
# my_file=open("text.txt","w")
# for i in banks_list:
#           my_file.write(i)

banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
my_file=open("text.txt","w")
for i in banks_list:
          my_file.write("%i\n"%i)

