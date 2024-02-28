s=input("enter a string : ")

al=0
num=0
sp=0
uc=0
lc=0

for i in s:
    if i.isalpha():
        al=al+1
    elif i.isspace():
        sp=sp+1
    elif i.isnumeric():
        num=num+1
    if i.isupper():
        uc=uc+1
    elif i.islower():
        lc=lc+1


print("total number of alphabets : ", al)
print("total number of space : ", sp)
print("total number of number : ", num)
print("total number of uppercase : ", uc)
print("total number of lowercase : ", lc)

