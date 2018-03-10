import codecs as cod

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

def feladat_10():
    try:
        fajl=open("be.txt", mode="r")
        max = 0
        for sor in fajl:
            sor = sor.strip()
            hossz = 0
            if sor[0].isupper():
                hossz+=len(sor)
                if max < hossz:
                    max = hossz
        print(max)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_11():
    try:
        fajl=open("be.txt", mode="r")
        min = 5000
        for sor in fajl:
            sor = sor.strip()
            hossz = 0
            if sor[len(sor)-1] == "!" or sor[len(sor)-1] == "?" or sor[len(sor)-1] == ".":
                hossz += len(sor)
                if min > hossz:
                    min = hossz
        print(min)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_15():
    try:
        fajl1 = open("be.txt", mode="r")
        fajl2 = open("ki.txt", mode="w")
        str = ""
        for sor in fajl1:
            sor = sor.strip()
            str+=sor
            if sor == "":
                break
        fajl2.write(str)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl1.close()
        fajl2.close()

def feladat_18():
    try:
        fajl = open("be.txt", mode="r")
        sor = fajl.readline()
        sor = sor.strip()
        sor = sor.split()
        score = sor[3].split(":")
        pont1 = int(score[0])
        pont2 = int(score[1])
        team1 = sor[0]
        team2 = sor[2]
        #print(team2, pont2)
        for sor in fajl:
            sor = sor.strip()
            sor = sor.split()
            score = sor[3].split(":")
            pont3 = int(score[0])
            pont4 = int(score[1])
            if sor[0] == team1:
                pont1+=pont3
                pont2+=pont4
            else:
                pont1+=pont4
                pont2+=pont3
        if pont1>pont2:
            print(team1, "nyert")
        elif pont2>pont1:
            print(team2, "nyert")
        else:
            print("dontetlen")
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_19():
    try:
        fajl = open("be.txt", mode="r")
        max = 0
        for sor in fajl:
            sor = sor.strip()
            sor = sor.split()
            latogatok = int(sor[1])
            if latogatok>max:
                max=latogatok
                tmp = sor[0]
        print(tmp)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_20():
    try:
        fajl = cod.open("be.txt", encoding="utf-8", mode="r")
        max = 0
        for sor in fajl:
            sor = sor.strip()
            sor = sor.split(";")
            lakosok = int(sor[2])
            if lakosok>max:
                max=lakosok
                tmp = sor[0]
        print(tmp)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl.close()

def feladat_21():
    try:
        fajl1 = open("be.txt", mode="r")
        fajl2 = open("ki.txt", mode="w")
        for sor in fajl1:
            sor = sor.strip()
            sor = sor.split(";")
            sum = 0
            for i in range(1, len(sor)):
                sum+=int(sor[i])
            fajl2.write("%s %d %s" % (sor[0], sum, '\n'))
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl1.close()
        fajl2.close()

def feladat_22():
    try:
        fajl1 = open("be.txt", mode="r")
        fajl2 = open("ki.txt", mode="w")
        min = 10000
        for sor in fajl1:
            sor = sor.strip()
            sor = sor.split(";")
            ido = float(sor[2])
            if ido<min:
                min=ido
                tmp = sor[0]
        fajl2.write(tmp)
    except OSError as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        fajl1.close()
        fajl2.close()


def main():
    print(feladat_1(8))
    print(feladat_2(5))
    feladat_3(513)
    feladat_4()
    feladat_5(10) # nincs kész
    print(feladat_6(807, 858))
    feladat_8(21)
    feladat_9()
    feladat_10()
    feladat_11()
    feladat_15()
    feladat_18()
    feladat_19()
    feladat_20()
    feladat_21()
    feladat_22()
main()