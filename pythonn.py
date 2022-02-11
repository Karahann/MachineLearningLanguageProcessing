import re

f = open('sorular.txt','r',encoding="utf-8")
x = open('stopwords.txt','r',encoding="utf-8")
sorular = f.read().lower()
yasakliKelimeler = x.read().lower()

list1 = []
list1 = sorular.split("\n")
list2 = []
list2 = yasakliKelimeler.split("\n")
list3 = []
sayac=0

for cumleler in list1:
    list1[sayac] = re.sub(r'[^\w\s]','', cumleler)
    kelimeler= list1[sayac].split(" ")
    for kelime in kelimeler:
        if kelime not in list2:
            list3.append(kelime)

allWords={}
for word in list3:
    if word not in allWords:
        allWords[word] = 1
    else:
        allWords[word] += 1

for key in allWords.keys():
   "Word: %s =>%s " %(key , allWords[key])

sort_orders = sorted(allWords.items(),key= lambda x: x[1],reverse=True)
dictionary={}
x=0
dictionary = { sort_orders[i][0] : i for i in range(0, 101) }
dictionary["OOV"] = 101

print(dictionary)

input = input("lutfen cumle girisi yapiniz: ").split(" ")
vector = []
for z in input:
    dizi=[]
    dizi = [0 for i in range(101)]
    print(len(dizi))
    
    if z in dictionary:
        vector.append(dictionary[z])
        dizi[dictionary[z]] = 1
    else:
        vector.append(dictionary["OOV"])
        dizi[dictionary["OOV"]-1] = 1
    print(dizi)

print(vector)