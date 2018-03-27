import numpy as np

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

def feladat_7():
    lista = []
    szam = int(input("Adj meg egy egesz szamot: "))
    lista.append(szam)
    while szam != 0:
        szam = int(input("Adj meg egy egesz szamot: "))
        if szam == 0:
            break
        lista.append(szam)
    for i in range(3):
        max = lista[0]
        for elem in lista:
            if elem > max:
                max = elem
        print(max, end=' ')
        lista.remove(max)

def feladat_8(n, t):
    for i in range(n-1):
        if not t[i]<=t[i+1]:
            return False
        else:
            continue
    return True

def feladat_10(k, t):
    t = sorted(t)
    print(t)
    ah = 0
    fh = len(t)-1
    while ah <= fh:
        i = (ah+fh)//2
        osztok_szama = 0
        for j in range(1, t[i]+1):
            if t[i] % j == 0:
                osztok_szama+=1
        if osztok_szama > k:
            return t[i]
        else:
            ah = i+1
    return -1

def feladat_11():
    sor = int(input("Add meg a sorok szamat: "))
    oszlop = int(input("Add meg az oszlopok szamat: "))
    matrix = np.zeros((sor,oszlop), dtype=int)
    for i in range(sor):
        for j in range(oszlop):
            matrix[i][j] = input("Add meg az elemeket sorfolytonosan: ")
    print(matrix)
    for j in range(oszlop):
        neg_db = 0
        null_db = 0
        for i in range(sor):
            if matrix[i][j] == 0:
                null_db+=1
            if matrix[i][j] < 0:
                neg_db+=1
        if null_db*2 <= neg_db:
            return (j,', ')

def feladat_12(a):
    for i in range(4):
        for j in range(3):
            if (i+j) == 0 or a[i][j] == 0:
                j+=1
            elif a[i][j] % (i+j) == 0:
                print(a[i][j], end=',')

def feladat_13(b):
    for j in range(3):
        min = b[0][j]
        for i in range(4):
            if b[i][j] < min:
                min = b[i][j]
        for i in range(4):
            b[i][j]-=min
    return b

def feladat_14(c):
    print(c)
    max = c[2][2]
    for i in range(2, 0, -1):
        j = 2
        while i+j >= 4:
            if c[i][j] > max:
                max = c[i][j]
            j-=1
    return max

def feladat_15(d, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                if not d[i][j] == 0:
                    return False
    return True

def feladat_16(e, f):
    for i in range(2):
        for j in range(3):
            f[j][i] = e[i][j]
    print(f)

def feladat_19(n, m):
    hatos = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n//2 or i == n-1:
                hatos[i][j] = 42
            else:
                hatos[i][j] = 32
        hatos[i][0] = 42
        if i > n//2:
            hatos[i][m-1] = 42
    for i in range(n):
        for j in range(m):
            print(chr(int(hatos[i][j])), end = '')
        print('\n')

def main():
    feladat_1()
    feladat_2()
    print(feladat_3())
    feladat_4()
    print(feladat_5())
    feladat_7()
    print(feladat_8(6, [4.6, 5.4, 5.5, 5.6, 5.6, 10.8]))
    print(feladat_10(4, [3, 7, 14, 12, 18, 5, 24])) #nem jo valamiert
    print(feladat_11()) #ez se jo valamiert minidg 0-t ad vissza
    a = np.array([[5,4,1],[0,2,1],[6,4,4],[0,0,1]])
    feladat_12(a)
    b = np.array([[5, 4, 1], [0, 2, 1], [6, 4, 4], [0, 3, 1]])
    print(feladat_13(b))
    c = np.array([[5, 4, 1], [0, 2, 1], [6, 5, 4]])
    print(feladat_14(c)) #nem a legnagyobbat adja meg
    d = np.array([[0, 4, 1], [0, 0, 1], [6, 5, 0]])
    print(feladat_15(d, 3))
    e = np.array([[0, 4, 1], [0, 0, 1]])
    f = np.zeros((3, 2))
    feladat_16(e, f)

    esetek = int(input())
    t = np.zeros(2*esetek, dtype = 'int')
    for i in range(0, 2*esetek, 2):
        sor = input()
        sor = sor.strip()
        sor = sor.split()
        t[i] = int(sor[0])
        t[i+1] = int(sor[1])

    for i in range(0, 2*esetek, 2):
        feladat_19(t[i], t[i+1])
main()