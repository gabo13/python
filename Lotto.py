# -*- Coding:Utf-8 -*-
from urllib.request import urlopen
import re, ssl
URL = "https://bet.szerencsejatek.hu/cmsfiles/otos.csv"
# file letöltése
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urlopen(URL, context=ctx)
with open("otos.csv", "wb") as f:
    f.write(response.read())
# file betöltése data nevü 2d-s tömbbe
data = []
with open("otos.csv", "r") as f:
    for line in f:
        temp = list(line.rstrip().split(";"))
        temp = list(map(int,temp[0:2]+temp[11:16]))
        data.append(temp)
data.reverse()
print("Lottószámok sikeresen letöltve a %s webhelyről."% URL)
#print(data)
stat1 = [0]*90 #90 elemü lista feltöltve 0-val
stat2 = [0]*90
stat3 = [0]*90
stat4 = [0]*90
stat5 = [0]*90
szum = [0]*90
def statisztika(data):
    print("---------------------------")
    print("     szám statisztika      ")
    print("       előfordulás         ")
    print("---------------------------")
    print("szám, húzás1...húzás5, összesen")
    
    for line in data:
        stat1[line[2]-1]=stat1[line[2]-1]+1
        stat2[line[3]-1]=stat2[line[3]-1]+1
        stat3[line[4]-1]=stat3[line[4]-1]+1
        stat4[line[5]-1]=stat4[line[5]-1]+1
        stat5[line[6]-1]=stat5[line[6]-1]+1
    for i in range(0,90):
        szum[i] = stat1[i]+stat2[i]+stat3[i]+stat4[i]+stat5[i]
        print("|{0:3d} | {1:3d} | {2:3d} | {3:3d} | {4:3d} | {5:3d} | {6:3d}".format(i+1,stat1[i],stat2[i],stat3[i],stat4[i],stat5[i],szum[i]))
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Pyplot not installed")
    value = range(0,90)
    plt.plot(value,szum, color='r')
    plt.plot(value,stat1, color='g')
    plt.plot(value,stat2, color='b')
    plt.plot(value,stat3, color='y')
    plt.plot(value,stat4, color='m')
    plt.plot(value,stat5, color='k')
    plt.ylabel('Előfordulás')
    plt.show()
    
     

def keres(data, numbers, talalat):
    """databan keres numberst és a találatnál nagyobbat kiírja"""
    print("---------------------------")
    print("       szám keres          ")
    #print("---------------------------")
    print("A keresett számok: ",numbers)
    for line in data:
        A=set(line[2:])
        B=set(numbers)
        intersect = sorted(A&B)
        #print(A, B, intersect)
        if len(intersect) >= talalat:
            print("{0} találat: {1:9s} {2:14s}".format(len(intersect), ' '.join(map(str,line[:2])), ' '.join(map(str,line[2:]))))

def findInFile(filename, talalat):
    with open(filename,'r') as f:
        for line in f:
            numbers = re.findall(r"(\d+)",line)
            numbers = list(map(int,numbers))
            #print(numbers)
            keres(data,numbers, talalat)
            
def  savetoFile(filename):
    with open(filename, 'w') as f:
        for line in data:
            f.write(' '.join(map(str,line[2:]))+'\n')
def menu():
    while True:
        print("******************************************")
        print("1.-Statisztika\n2.-Keresés\n3.-Kiléps\n4.-Kereses fajlból\n")
        vez_inp =input("Kérek egy számot: ")
        if vez_inp == '1':
            statisztika(data)
        elif vez_inp == '2':
            numbers = re.findall(r"(\d+)",input("Kérem a számokat: "))
            keres(data,list(map(int,numbers)), 2)
        elif vez_inp=='3':
            break;
        elif vez_inp=='4':
            findInFile(input("Kérem a fájl nevét (saját számok): "),
            int(input("Hány találatos szelvényeket írjon ki?(1-5): ")))
                      
    

savetoFile('szamok.txt')

    

"""
statisztika(data)
keres(data, ["1","2","3","4","5"])
print("PROGRAM END")
text = "1, 2, 3, 4, 50"
import re
pattern = r"(\d+)"
mach = re.findall(pattern, text)
print("Mach: ",mach)
"""
menu()



