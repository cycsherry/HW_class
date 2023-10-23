poly=input("input the polynomial:")
listp=list(poly)
lists=[]
for i in listp:
    a=listp.index(")")
    list1=listp[1:a]
    lists.append(list1)
    del listp[0:a+1]
# print(lists)
for i in range(len(lists)):
    index=[]
    for k,v in enumerate(lists[i]):
        if v=="-":
            index.append(k)
        elif v =="+":
            index.append(k)
    index.reverse()
    list1=[]
    for a in index:
        var1="".join(lists[i][a:])
        list1.append(var1)
        del lists[i][a:]
    list1.reverse()
    str1="".join(lists[i])
    list1.insert(0,str1)
    lists[i]=list1
    plus=[]
    for l in lists[i]:
        if "+" == l[0]:
            l=l[1:]
            plus.append(l)
        else:
            plus.append(l)
    lists[i]=plus

# print(lists)

for i in range(len(lists)):
    for l in range(len(lists[i])):
        str1=lists[i][l]  
        indexr=[]
        for k,v in enumerate(str1):
            if v=="^":
                indexr.append(k)
        indexr.reverse()
        str2=[]
        if indexr !=[] :
            for m in indexr:
                int1=[]
                for k in str1[m:]:
                    if k.isdigit()==True:
                        int1.append(k)
                        left=""
                    elif k.isdigit()==False and k!=("^"):
                        f=str1.index(k)
                        left=str1[f:]
                int2="".join(int1)
                # print(int2)
                r=1
                mul=str1[m-1]
                while r<int(int2):
                    mul=mul+str1[m-1]
                    r=r+1 
                str2.append(mul)
                # print(str2)
                str1=str1[:m-1]
                # print(str1)
                int1=[]
            str2.reverse()
            str3="".join(str2)
            lists[i][l]=str1+str3+left
# print(lists)

listsm=[]
i=0
while i < len(lists):
    for l in range(len(lists[0])):
        minus=0
        if lists[0][l][0]=="-":
            lists[0][l]=lists[0][l][1:]
            minus=1
        if ("*") in lists[0][l]:
            k=lists[0][l].find("*")
            var4="".join(lists[0][l][k+1:]) #字串
            intk=int(lists[0][l][:k]) #常數
            # print(intk,var4)
        else:
            if lists[0][l].isdigit():
                intk=int(lists[0][l])
                var4=""
            else:
                intk=1
                var4=lists[0][l]
            # print(intk,var4)
        if minus==1:
            intk=intk*(-1)
        for r in range(len(lists[1])):
            minus1=0
            a=lists[1][r]
            if lists[1][r][0]== ("-"):
                lists[1][r]=lists[1][r][1:]
                minus1=1
                # print(minus1)
            if ("*") in lists[1][r]:
                g=lists[1][r].find("*")
                var5="".join(lists[1][r][g+1:]) #字串
                intg=int(lists[1][r][:g]) #常數
                # print(intg,var5)
            else:
                if lists[1][r].isdigit():
                    intg=int(lists[1][r])
                    var5=""
                else:
                    intg=1
                    var5=lists[1][r]
            if minus1==1:
                intg=intg*(-1)
            lists[1][r]=a
            result=str(intk*intg)+"*"+var4+var5
            listsm.append(result)
    del lists[1]
    del lists[0]
    lists.insert(0,listsm)
    listsm=[]
    i=i+1
listsf=lists[0]

# print(listsf)

for l in listsf:
    k=l.rstrip("*")
    listsf.append(k)
    listsf.remove(l)
listsf.sort()
# print(listsf)

listc=[]
for g in range(len(listsf)):
    dict1={}
    listst=[]
    for k in listsf[g]:
        if k.isdigit() == False and listsf[g].count(k) >=1 and k!="*" and k!="-":
            dict1.setdefault(k,listsf[g].count(k))
    listst.append(g)
    listst.append(list(sorted(dict1.items())))
    listc.append(listst)
# print(listc)

listsff=[]
for n in range(len(listc)):
    index=[]
    for m in range(len(listc)):
        if listc[m][1] == listc[n][1]:
            index.append(listc[m][0])
    coe=[]
    if len(index)>1:
        for k in index:
            a=listsf[k].index("*")
            stra=[]
            strc=[]
            if ("-") in listsf[k]:
                for l in listsf[k]:
                    if l.isdigit()==True:
                        stra.append(l)
            elif ("-") not in listsf[k]:
                for l in listsf[k]:
                    if l.isdigit()==True:
                        strc.append(l)
            if stra!=[]:
                stra.insert(0,"-")
                strb="".join(stra)
                coe.append(int(strb)) 
            elif strc!=[]:
                strd="".join(strc)
                coe.append(int(strd))
            elif stra==[] and strc==[]:
                if ("-") not in listsf[k]:
                    strc.append("1")
                    strd="".join(strc)
                    coe.append(int(strd))
                elif ("-") in listsf[k]:
                    stra.append("-1")
                    strb="".join(stra)
                    coe.append(int(strb))
        a=listsf[k].index("*")
        b=sum(coe)
        c="".join(listsf[index[0]][a:])
        f=str(b)+c
        listsff.append(f)
    else:
        a=listsf[index[0]]
        listsff.append(a)
nice=list(set(listsff))
# print(nice)

for g in range(len(nice)):
    repeat={}
    repeat_alpha=[]
    for k in nice[g]:
        if nice[g].count(k) >1 and k.isalpha():
            repeat.setdefault(k,nice[g].count(k))
            repeat_alpha.append(k)
    # print(repeat)
    repeat_a=list(set(repeat_alpha))
    # print(repeat_a)
    if repeat !={}:
        for a in repeat_a:
            str1=nice[g]
            new_str=list(set(str1))
            # print(new_str)
            final=sorted(new_str,key=str1.index)
            # print(final)
            final.insert((final.index(a)+1),"^")
            final.insert((final.index(a)+2),str(repeat[a]))
            # print(final)
            nice[g]="".join(final)
            # print(nice[g])
# print(nice)
a=nice[0]
for k in nice:
    if k[0] !="-":
        a=a+"+"+k
    else:
        a=a+k
print(a)
        






            
            
