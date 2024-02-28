file=open("tops1.txt","w")
file.write("this is file management demo using python.")
file.close()
print("file written successfully")
print("*****************************************************")


file=open("tops1.txt","r")
print(file.read())
file.close()
print("******************************************************")


file=open("tops1.txt","a")
file.write("\nthis file is now appended.")
file.close()
print("file Appended successfully")
print("**************************************************")


file=open("tops1.txt","r")
print(file.read())
file.close()
print("***************************************************")



file=open("tops2.txt","w+")
file.write("this is w+ opration is python.")
print("current file position : " ,file.tell())
file.seek(20)
print(file.read())
file.close()
print("************************************************")

