import math

def feladat_1(a, b):
    a,b = b,a
    print(a, b)

def feladat_2():
    t=[]
    for k in range(3):
        szam = int(input("Add meg a szamot: "))
        t.append(szam)
    for i in range(2):
        minhely=i
        for j in range(i+1, 3):
            if t[j]<t[minhely]:
                minhely=j
        if minhely != i:
            temp = t[i]
            t[i] = t[minhely]
            t[minhely] = temp
    print(t)

def feladat_3(x):
    if -2<x<0:
        return 2*x
    elif 0<=x<2:
        return x*x
    elif x>2:
        return 10
    return "A fuggveny nem definialt ilyen x-re"

def feladat_4(valos1, valos2, valos3):
    t = [valos1, valos2, valos3]
    min = t[0]
    for i in range(1, 3):
        if t[i] < min:
            min = t[i]
    return min

def feladat_5(a, b, c, d):
    print(a, b, c, d)
    if d >= 0:
        print(a, c, b, d)
    else:
        print(a, b, d, c)

def feladat_6(a, b, c):
    if a<b+c and b<a+c and c<a+b:
        s = (a+b+c)/2
        be_sugar = math.sqrt((s-a)*(s-b)*(s-c)/s)
        print(be_sugar)
        ki_sugar = a*b*c/(4*math.sqrt((s*(s-a)*(s-b)*(s-c))))
        print(ki_sugar)
    else:
        print("a haromszog-egyenlotlenseg fuggvenyeben nem alkothatnak haromszoget")

def feladat_7(a, b, drot):
    kerulet = 2*(a+b)
    if kerulet > drot:
        print(kerulet-drot, "drot szukseges meg a kert bekeritesehez")
    else:
        print(drot-kerulet, "drotunk marad a kert bekeritese utan")

def feladat_8(x, a, b, c, d):
    if x<5:
        print(3*x-5)
    elif 5<=x<=10:
        print(10)
    elif x>10:
        print(9*x+1)
    if a+c>2*d and b>0:
        print(d-3*b)
    elif a+c<2*d and b<0:
        print(d+3*b)
    else:
        print(4)

def feladat_9(a, b, c):
    D = b*b-4*a*c
    if D < 0:
        return 0
    elif D == 0:
        return (-b/2*a)
    else:
        return ((-b+math.sqrt(D))/2*a) ((-b-math.sqrt(D))/2*a)

def feladat_10(tol, ig):
    szokoev = 0
    for i in range(tol, ig+1):
        if i%4 == 0 and i%100 !=0 or i%400 == 0:
            szokoev+=1
    return szokoev

def feladat_11(szul_datum):
    datum = szul_datum.split(".")
    eredmeny = 365*(2018-int(datum[0]))+30*(2-int(datum[1]))+(23-int(datum[2]))
    print(eredmeny)

def feladat_12(elert, max):
    if elert/max*100 >= 60:
        print("sikeres zh")
    else:
        print("megbukott")

def feladat_13(erdemjegy):
    if erdemjegy==1:
        print("egyes")
    elif erdemjegy==2:
        print("kettes")
    elif erdemjegy==3:
        print("harmas")
    elif erdemjegy==4:
        print("negyes")
    elif erdemjegy==5:
        print("otos")

def feladat_14(sorszam):
    if sorszam==1:
        print("Januar")
    elif sorszam==2:
        print("Februar")
    elif sorszam==3:
        print("Marcius")
    elif sorszam==4:
        print("Aprilis")
    elif sorszam==5:
        print("Majus")
    elif sorszam==6:
        print("Junius")
    elif sorszam==7:
        print("Julius")
    elif sorszam==8:
        print("Augusztus")
    elif sorszam==9:
        print("Szeptember")
    elif sorszam==10:
        print("Oktober")
    elif sorszam==11:
        print("November")
    elif sorszam==12:
        print("December")

def feladat_15(a, b):
    hanyados = 0
    while a >= b:
        hanyados+=1
        a = a-b
    print(hanyados)

def feladat_16(a, b):
    lnko = 0
    r = a%b
    while r!=0:
        r=a%b
        a=b
        b=r
        lnko=a
    print(lnko)

def feladat_17(szam):
    masolat = szam
    ujszam = 0
    while szam > 0:
        szamjegy = szam%10
        ujszam = ujszam*10+szamjegy
        szam = szam//10
    if ujszam==masolat:
        print("igaz")
    else:
        print("hamis")


def feladat_18(a, b):
    x = a
    y = b
    p = 0
    while x > 0:
        if x%2 != 0:
            p+=y
        x = x//2
        y+=y
    print(p)

def feladat_19(n):
    osztok_szama = 0
    for oszto in range(1,n+1):
        if n%oszto == 0:
            osztok_szama+=1
    if osztok_szama == 2:
        return "igaz"
    else:
        return "hamis"

def feladat_20(n):
    a = 1
    b = 0
    for k in range(1,n+1):
        print(b)
        b+=a
        a = b-a

def feladat_21(n):
    ujszam = 0
    while n != 0:
        ujszam = ujszam*10+(n%10)
        n = n//10
    print(ujszam)

def feladat_22(x, n):
    eredmeny = 1
    while n > 0:
        if n%2 != 0:
            eredmeny*=x
            n-=1
        x*=x
        n = n//2
    print(eredmeny)

#def feladat_23(n):
#    tokeletes = 6
#    for i in range():

def feladat_24():
    db1 = 0
    db2 = 0
    szam = int(input("Kerem az elso szamot: "))
    while szam != 0:
        if szam%7 == 5:
            db1+=1
        if szam%13 == 7:
            db2+=1
        szam = int(input("Kovetkezo szam: "))
    print(db1, "darab 5 maradeku szam erkezett 7-tel osztva.")
    print(db2, "darab 7 maradeku szam erkezett 13-mal osztva.")

def feladat_25():
    szam1 = int(input("Kerlek add meg a lakosok szamat: "))
    szam2 = int(input("Kerlek add meg az orszag teruletet (km^2): "))
    nepsuruseg = szam1/szam2
    print("Az orszag nepsurusege: ",nepsuruseg, "fő/km^2")
    if nepsuruseg<=50:
        print("ritkan lakott terulet")
    elif 50<nepsuruseg<=300:
        print("atlagos nepsurusegu orszag")
    else:
        print("surun lakott orszag")

def feladat_26():
    szam = float(input("Kerem az elso szamot: "))
    db_poz = 0
    db_neg = 0
    if szam > 0:
        db_poz+=1
    elif szam < 0:
        db_neg+=1
    sum = szam
    print(sum)
    while sum != 0:
        szam = float(input("Kovetkezo szam: "))
        sum+=szam
        print(sum)
        if szam > 0:
            db_poz+=1
        elif szam < 0:
            db_neg+=1
    print(db_poz," pozitiv szam erkezett",'\n',db_neg," negativ szam erkezett")

def feladat_27():
    szam = int(input("Kerem az elso szamot: "))
    db_poz = 0
    db_neg = 0
    if szam > 0:
        db_poz+=1
    elif szam < 0:
        db_neg+=1
    while db_poz-1==db_neg or db_poz+1==db_neg or db_poz==db_neg:
        szam = int(input("Kerem a kovetkezo szamot: "))
        if szam > 0:
            db_poz+=1
        elif szam < 0:
            db_neg+=1
        if db_poz+2==db_neg or db_poz-2==db_neg:
            break
    print(db_poz, " pozitiv szam erkezett", '\n', db_neg, " negativ szam erkezett")

def feladat_28(n):
    lehetseges = int(math.sqrt(n))
    print(lehetseges*lehetseges)

def feladat_29(szam):
    if 0<=szam<=12:
        faktorialis = 1
        i = 1
        while i<=szam:
            faktorialis*=i
            i+=1
        print(faktorialis)

def feladat_30():
    rand_datum = input("Adj egy datumot: ")
    datum = rand_datum.split(".")
    hanyadik = int(datum[2])
    if datum[1] == "01":
        print(hanyadik)
    if datum[1] == "02":
        hanyadik+=31
        print(hanyadik)
    if int(datum[0])%4 == 0 and int(datum[0])%100 != 0 or int(datum[0])%400 == 0:
        if datum[1] == "03":
            hanyadik = hanyadik + 31 + 29
            print(hanyadik)
        elif datum[1] == "04":
            hanyadik = hanyadik + 31 + 29 + 31
            print(hanyadik)
        elif datum[1] == "05":
            hanyadik = hanyadik + 31 + 29 + 31 + 30
            print(hanyadik)
        elif datum[1] == "06":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31
            print(hanyadik)
        elif datum[1] == "07":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31 + 30
            print(hanyadik)
        elif datum[1] == "08":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31 + 30 + 31
            print(hanyadik)
        elif datum[1] == "09":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
            print(hanyadik)
        elif datum[1] == "10":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30
            print(hanyadik)
        elif datum[1] == "11":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            print(hanyadik)
        elif datum[1] == "12":
            hanyadik = hanyadik + 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
            print(hanyadik)
    else:
        if datum[1] == "03":
            hanyadik = hanyadik + 31 + 28
            print(hanyadik)
        elif datum[1] == "04":
            hanyadik = hanyadik + 31 + 28 + 31
            print(hanyadik)
        elif datum[1] == "05":
            hanyadik = hanyadik + 31 + 28 + 31 + 30
            print(hanyadik)
        elif datum[1] == "06":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31
            print(hanyadik)
        elif datum[1] == "07":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31 + 30
            print(hanyadik)
        elif datum[1] == "08":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31 + 30 + 31
            print(hanyadik)
        elif datum[1] == "09":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
            print(hanyadik)
        elif datum[1] == "10":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
            print(hanyadik)
        elif datum[1] == "11":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            print(hanyadik)
        elif datum[1] == "12":
            hanyadik = hanyadik + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
            print(hanyadik)

def feladat_31(n):
    ig = int(n/2)
    for i in range(1, ig+1):
        if n%i == 0:
            print(i, end=", ")
    print(100, '\n')

def feladat_32(k):
    n1 = int(input("mettol?: "))
    n2 = int(input("meddig?: "))
    for i in range(n1, n2+1):
        if i%k == 0:
            print(i, end=" ")

def feladat_38():
    szam = input("Adj egy max 9 szamjegyu egesz szamot! ")
    szamjegy = input("adj meg egy szamjegyet! ")
    db = 0
    for i in range(len(szam)):
        if szamjegy == szam[i]:
            db+=1
    print(db)


def main():
    feladat_1(5, 10)
    feladat_2()
    print(feladat_3(2))
    print(feladat_4(5, -3.5, 0))
    feladat_5(3, 5.2, 1.8, -1.2)
    feladat_6(3, 4, 5)
    feladat_7(5, 10, 30)
    feladat_8(5, 1, 4, 3, 2)
    print(feladat_9(1, 2, 1))
    print(feladat_10(1996, 2018))
    feladat_11("1996.01.18")
    feladat_12(30, 50)
    feladat_13(3)
    feladat_14(7)
    feladat_15(5, 2)
    feladat_16(360, 225)
    feladat_17(303)
    feladat_18(45, 17)
    print(feladat_19(7))
    feladat_20(11)
    feladat_21(321)
    feladat_22(2, 6)
#    feladat_23(2)
    feladat_24()
    feladat_25()
    feladat_26()
    feladat_27()
    feladat_28(225)
    feladat_29(0)
    feladat_30()
    feladat_31(100)
    feladat_32(2)
    feladat_38()
main()