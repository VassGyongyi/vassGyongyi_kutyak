from kutya import Kutya


kutya1 = Kutya("Foltos", "kan", "keverék", 50, 20)
kutya2 = Kutya("Cézár", "kan", "farkas", 55, 25)
kutya3 = Kutya("Csöpi", "nőstény", "tacskó", 15, 5)

kutya = [kutya1, kutya2, kutya3]
#kutya1.set_nev("Foltos")
def kutyak():
    i = 0
    fejlec = "{:<10}{:<10}{:<10}{:<15}{:<10}"
    print(fejlec.format("név","nem","fajta","marmagasság","súly"))
    while (i< len(kutya)):
        print(f"{kutya[i].get_nev():<10}"
              f"{kutya[i].nem:<10}"
              f"{kutya[i].fajta:<10}"
              f"{kutya[i].marmagassag:<15}"
              f"{kutya[i].suly:<10}")
        i += 1
def csinal():
    i = 0
    while (i < len(kutya)):
        valamit_csinal = kutya[i].tevekenyseg()
        if (valamit_csinal) == "ugat":
            print(f"{kutya[i].get_nev()}: {valamit_csinal}, harap")
        else:
                print(f"{kutya[i].get_nev()}: {valamit_csinal}")
        i += 1

def csinal2():
    i = 0
    print("\n")
    while (i < len(kutya)):
        valamit_csinal = kutya[i].tevekenyseg()
        if (valamit_csinal) == "ugat":
            print(f"{kutya[i].get_nev()}: {valamit_csinal},{harap(valamit_csinal)}")
        else:
            print(f"{kutya[i].get_nev()}: {valamit_csinal}")
        i += 1

def csinal3():
    i = 0
    while (i < len(kutya)):
        valamit_csinal = kutya[i].tevekenyseg()
        if (valamit_csinal) == "ugat":
           return kutya[i].get_nev()
        else:
            return "Egyik sem"
        i += 1

def harap(harapos):
    if harapos == "ugat":
        return "harap"

def harap2():
    nev = csinal3()
    print("\nÚjabb véletlen választás szerint: ")
    print(f"{nev} ugat és harap.")

kutyak()
#csinal()
csinal2()
harap2()



