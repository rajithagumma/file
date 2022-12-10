search_text="welcome"
replace_text="good morning"
file=open("sample_file.txt","r")
data=file.read()
data=data.replace(search_text,replace_text)
file=open("sample_file.txt","w")
file.write(data)
print("text replaced")