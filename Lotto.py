from urllib.request import urlopen
import re

# file letöltése
response = urlopen("https://bet.szerencsejatek.hu/cmsfiles/otos.csv")
with open("otos.csv", "wb") as f:
    f.write(response.read())
# file betöltése data nevü 2d-s tömbbe
data = []
with open("otos.csv", "r") as f:
    for line in f:
        temp = list(line.rstrip().split(";"))
        data.append(temp)

        
def statisztika(data):
    print("---------------------------")
    print("     szám statisztika      ")
    print("       előfordulás         ")
    print("---------------------------")
    print("szám, húzás1...húzás5, összesen")
    stat1 = {i:0 for i in range(1,91)} #90 elemü dictionary-k feltöltve 0-val
    stat2 = {i:0 for i in range(1,91)}
    stat3 = {i:0 for i in range(1,91)}
    stat4 = {i:0 for i in range(1,91)}
    stat5 = {i:0 for i in range(1,91)}
    for line in data:
        stat1[int(line[11])]=stat1[int(line[11])]+1
        stat2[int(line[12])]=stat2[int(line[12])]+1
        stat3[int(line[13])]=stat3[int(line[13])]+1
        stat4[int(line[14])]=stat4[int(line[14])]+1
        stat5[int(line[15])]=stat5[int(line[15])]+1
    for i in range(1,91):
        szum = stat1[i]+stat2[i]+stat3[i]+stat4[i]+stat5[i]
        print("|{0:3d} | {1:3d} | {2:3d} | {3:3d} | {4:3d} | {5:3d} | {6:3d}".format(i,stat1[i],stat2[i],stat3[i],stat4[i],stat5[i],szum))


def keres(data, numbers):
    print("---------------------------")
    print("       szám keres          ")
    print("       egyezés             ")
    print("---------------------------")
    print("A keresett számok: ",numbers)
    for line in data:
        A=set(line[11:])
        B=set(numbers)
        intersect = sorted(A&B)
        #print(A, B, intersect)
        if len(intersect) > 1:
            print("{:2d} találat:{} {}".format(len(intersect),line[:2],intersect))
def menu():
    while True:
        print("******************************************")
        print("1.-Statisztika\n2.-Keresés\n3.-Kiléps\n")
        vez_inp =input("Kérek egy számot: ")
        if vez_inp == '1':
            statisztika(data)
        elif vez_inp == '2':
            keres(data,re.findall(r"(\d+)",input("Kérem a számokat: ")))
        elif vez_inp=='3':
            break;
            
    



    

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



