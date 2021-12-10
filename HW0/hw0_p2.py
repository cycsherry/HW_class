fin=open("IMDB-Movie-Data.csv","rt")
lines=fin.readlines()
lists=[]

dict1={}
rating=[]
list_danda=[]
dict2={}
dict4={}
list_aandr=[]
list_aandg=[]
dict6={}
dict8={}

for i in range(1,len(lines)):
    lists1=list(lines[i].split(","))
    lists.append(lists1)
    if lists1[5] =="2016":
        dict1.setdefault(lists1[1],float(lists1[7]))
        
#第一題
lists_rate=sorted(list(dict1.values()),reverse=True)
top3=lists_rate[0:3]
a=list(dict1.keys())[list(dict1.values()).index(top3[0])]
b=list(dict1.keys())[list(dict1.values()).index(top3[1])]
c=list(dict1.keys())[list(dict1.values()).index(top3[2])]

print("1. Top-3 movies with the highest ratings in 2016 :")
print("  no.1:",a,",no.2:",b,",no.3:",c)

#第二題
for l in range(len(lists)):
    actor=lists[l][4].split("|")
    for i in actor:
        list2=[]
        if lists[l][9] != "":
            list2.append(i.lstrip())
            list2.append(float(lists[l][9]))
            list_aandr.append(list2)
list_aandr.sort()

for m in range(len(list_aandr)):
    revenue=[]
    c=0
    for k in range(len(list_aandr)):
        if list_aandr[k][0]==list_aandr[m][0]:
            revenue.append(float(list_aandr[k][1]))
            c=c+1
    dict4.setdefault(list_aandr[m][0],sum(revenue)/c)
dict5=sorted(dict4.items(),key=lambda d:d[1],reverse=True)
no4=[]
for i in range(len(dict5)):
    if dict5[i][1]==dict5[0][1]:
        no4.append(dict5[i][0])
var4=", ".join(no4)
print("2. The actor generating the highest average revenue:")
print("  ",var4)

#第三題
for l in range(len(lists)):
    actor1=lists[l][4].split("|")
    list2=[]
    for i in actor1:
        actor=i.lstrip()
        list2.append(actor)
    if "Emma Watson" in list2:
        rating.append(float(lists[l][7]))

avr=sum(rating)/len(rating)
print("3. The average rating in Emma Watson's movie is",avr)

#第四題
for l in range(len(lists)):
    danda=[]
    actor=lists[l][4].split("|")
    list2=[]
    for i in actor:
        list2.append(i.lstrip())
    danda.append(lists[l][3])
    danda.append(list2)
    list_danda.append(danda)
list_danda.sort()

for m in range(len(list_danda)):
    actor=[]
    for k in range(len(list_danda)):
        if list_danda[k][0]==list_danda[m][0]:
            for i in list_danda[k][1]:
                actor.append(i)
        a=len(set(actor))
    dict2.setdefault(list_danda[m][0],a)
dict3=sorted(dict2.items(),key=lambda d:d[1],reverse=True)
no3=[]
for i in range(len(dict3)):
    if dict3[i][1]==dict3[2][1]:
        no3.append(dict3[i][0])
var3=", ".join(no3)
print("4. Top-3 directors who collaborate with the most actors:")
print("  No.1:",dict3[0][0])
print("  No.2:",dict3[1][0])
print("  No.3:",var3)

#第五題
for i in range(len(lists)):
    genre=lists[i][2].split("|")
    actor=lists[i][4].split("|")
    list2=[]
    for i in actor:
        list2.append(i.lstrip())
    for l in list2:
        list3=[]
        list3.append(l)
        list3.append(genre)
        list_aandg.append(list3)
        
for m in range(len(list_aandg)):
    genre2=[]
    for k in range(len(list_aandg)):
        if list_aandg[k][0]==list_aandg[m][0]:
            for i in list_aandg[k][1]:
                genre2.append(i)
        a=len(set(genre2))
    dict6.setdefault(list_aandg[m][0],a)
dict7=sorted(dict6.items(),key=lambda d:d[1],reverse=True)
no2=[]
for i in range(len(dict7)):
    if dict7[i][1]==dict7[1][1]:
        no2.append(dict7[i][0])
print("5. The top2 actors playing in the most genres of movies:")
print("  no1:",dict7[0][0])
no=", ".join(no2)
print("  no2:",no)

#第六題
list_actor1=[]   
for i in range(len(lists)):
    lists[i][4]=lists[i][4].split("|")
    lista=[]
    for l in lists[i][4]:
        lista.append(l.lstrip())
        list_actor1.append(l.lstrip())
        lists[i][4]=lista   
list_actor=list(set(list_actor1))
list_actor.sort()

for k in list_actor:
    year=[]
    for r in range(len(lists)):
        if k in lists[r][4]:
            year.append(int(lists[r][5]))
    a=max(year)-min(year)
    dict8.setdefault(k,a)
dict9=sorted(dict8.items(),key=lambda d:d[1],reverse=True)
aa=[]
for i in range(len(dict9)):
    if dict9[i][1]==dict9[0][1]:
        aa.append(dict9[i][0])
a1=", ".join(aa)
bb=[]
for i in range(len(dict9)):
    if dict9[i][1]==dict9[1][1]:
        bb.append(dict9[i][0])
b1=", ".join(bb)
cc=[]
for i in range(len(dict9)):
    if dict9[i][1]==dict9[2][1]:
        cc.append(dict9[i][0])
c1=", ".join(cc)
print("6. Top3 actors whose movies lead to the largest maximum gap of years:")
print(" no.1:",a1)

#第七題
johnny=[]
list_actor=[]
for l in range(len(lists)):
    actor=lists[l][4].split("|")
    list2=[]
    for i in actor:
        list2.append(i.lstrip())
    list_actor.append(list2)
    for l in list2:
        if "Johnny Depp" in list2:
            johnny.append(l)
johnny1=set(johnny)
h=set()
while h != johnny1:
    h=johnny1
    for k in list_actor:
        for r in johnny1:
            if r in k:
                johnny1=set(k)|johnny1
print("7. ",len(johnny1))
        
        


fin.close()                
