ch=input()
c=0
for i in range (len(ch)):
    if(ch[i].isdigit()or ch[i].isalpha() or ch[i]==' '):
        continue
    else:
        c+=1
print(c)
