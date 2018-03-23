def feladat_1():
    n = int(input("Adj meg egy egesz szamot: "))
    t = []
    i = 0
    while i < n:
        szam = int(input("Adj meg egy egesz szamot: "))
        t.append(szam)
        i+=1
    for j in range(n-1):
        if t[j] == t[j+1]:
            print(j+1, j+2)

def feladat_2():
    n = int(input("Adj meg egy egesz szamot 1 es 100 kozott: "))
    i = 0
    paros = 0
    paratlan = 0
    while i < n:
        szam = int(input("Adj meg egy egesz szamot: "))
        if szam % 2 == 0:
            paros+=1
        else:
            paratlan+=1
        i += 1
    print("Az arany:", "%d%s%d" % (paros,":",paratlan))

def feladat_3():
    n = int(input("Adj meg egy egesz szamot: "))
    t = []
    i = 0
    while i < n:
        szam = float(input("Adj meg egy egesz szamot: "))
        t.append(szam)
        i += 1
    sum = 0
    for elem in t:
        if elem < 0:
            elem = -elem
        sum+=elem
    return sum/n

def feladat_4():
    n = int(input("Adj meg egy egesz szamot: "))
    i = 0
    szorzat = 1
    sum = 0
    db = 0
    db_poz = 0
    while i < n:
        szam = float(input("Adj meg egy egesz szamot: "))
        if szam > 0:
            szorzat*=szam
            db_poz+=1
        elif szam < 0:
            sum+=szam
            db+=1
        i += 1
    if db_poz == 0:
        print("nem erkezett pozitiv szam: ",szorzat-1)
    else:
        print("A pozitiv szamok szorzata: ", szorzat)
    if db == 0:
        print("0-val valo osztas nem definialt, nem erkezett negativ input")
    else:
        print("A negativ szamok szamtani kozepe: ",sum/db)

def feladat_5():
    n = int(input("Adj meg egy egesz szamot: "))
    t = []
    i = 0
    while i < n:
        szam = int(input("Adj meg egy termeszetes szamot: "))
        t.append(szam)
        i += 1
    sum = 0
    szorzat = 1
    for elem in t:
        if elem < 7:
            szorzat*=elem
        elif elem > 10:
            sum+=elem
    return (szorzat, elem)

def main():
    feladat_1()
    feladat_2()
    print(feladat_3())
    feladat_4()
    print(feladat_5())
main()