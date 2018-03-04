def feladat_1(n):
    osztok_szama = 0
    szam = int(n)
    for oszto in range(2,(szam//2)+1):
        if szam%oszto == 0:
            osztok_szama+=1
    if osztok_szama == 2:
        return "IGAZ"
    else:
        return "HAMIS"

def feladat_2(n):
    primek = []
    for i in range(1,1000):
        osztok_szama = 0
        for k in range(1,i+1):
            if i%k == 0:
                osztok_szama+=1
        if osztok_szama == 2:
            primek.append(i)
    return primek[n-1]

def feladat_3(n):
    hatvanyok = []
    for i in range(0,20):
        hatvanyok.append(2**i)
    for elem in hatvanyok:
        if elem == n:
            print(n)

def feladat_4():
    for i in range(100,1000):
        i = str(i)
        if i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
            print(i, end=',')
    print('\n')

def feladat_5(n):
    osszetett = []
    for i in range(1,n+1):
        osztok_szama = 0
        for k in range(1, i + 1):
            if i % k == 0:
                osztok_szama += 1
        osszetett.append(i)
        osszetett.append(osztok_szama)
    print(osszetett)

def feladat_6(szam1, szam2):
    szam1 = str(szam1)
    szam2 = str(szam2)
    kozos = 0
    for i in range(len(szam1)):
        for k in range(len(szam2)):
            if szam1[i] == szam2[k]:
                kozos+=1
                break
    if kozos >= 2:
        return True
    else:
        return False

def feladat_8(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
        if sum>=n:
            break
    print(i)

def feladat_9():
    perc = 2
    m = 1
    while m <= 300:
        m = m+m*(1/perc)
        perc+=1
    print(perc-2)

def main():
    print(feladat_1(8))
    print(feladat_2(5))
    feladat_3(513)
    feladat_4()
    feladat_5(10) # nincs kész
    print(feladat_6(807, 858))
    feladat_8(21)
    feladat_9()
main()