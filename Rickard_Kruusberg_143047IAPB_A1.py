import time

import random

print("Tegemist on topsimänguga! Versioon 1.1.1 \n")
print("""Tegemist on tavalise topsimänguga. Valida tuleb kolme topsi vahel,
millest ühel on münt topsi sisse peidetud. Juhendid kuvatakse
mängu käigus. Head mängimist!""")

mängu_alustamis_korrad = 0

while True:

    mängu_alustamis_korrad += 1

    print('\n')    
    kas_alustada = input("Kas soovite alustada mängu? Jah/Ei ")

    if kas_alustada.lower() == "jah":
        print("Palun oota, topse segatakse!")
        time.sleep(5)
        print('\n')
        print("Arva, millises topsis on münt!")

        mündi_asukoht = random.randint(0,3)
        mängija_arvamine = input("Sisestage topsi number (1, 2 või 3): ")

        if mängija_arvamine.isdigit() == True:
            if int(mängija_arvamine) == mündi_asukoht:
                print("Ära arvasid!")
                mängu_alustamis_korrad = 0
            elif int(mängija_arvamine) < 1 or int(mängija_arvamine) > 3:
                print("Sisestatud väärtus peab jääma vahemikku 1-3!")
                mängu_alustamise_korrad = 0
            else:
                print("Ei arvanud ära!")
                mängu_alustamis_korrad = 0
        else:
            print("Peab olema arv vahemikus 1-3!")
        

    elif kas_alustada.lower() == "ei":
        print("Mäng on lõppenud!")
        break
    elif mängu_alustamis_korrad > 2:
        print("Sisestasite valed valikud, mäng katkestatakse. Kontrollige oma süsteemi.")
        break
    else:
        print("Sisestasite valesti. Palun korrake oma valikut: ")

