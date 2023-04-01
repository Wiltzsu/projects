import db
import datetime
from oliot import Pelaaja, Joukkue, Ottelu

def kirjautuminen():
    while True:
        print("TURNAUS KIRJAUTUMINEN")
        print("-" * 90)
        nimi = input("Nimi: ")
        if db.login(nimi, 4):
            break
        else:
            print("\nTunnuksesi eivät riitä kirjautumiseen. Yritä uudelleen.\n")

def alku_valinta():
    print("KOMENTOVALIKKO")
    print("-" * 90)
    print("1 - Pelaajat ")
    print("2 - Joukkueet ")
    print("3 - Ottelut")
    print("exit - Lopeta ohjelma")
    print("-" * 90)

def display_pelaajat():
    print("KOMENTOVALIKKO (PELAAJAT)")
    print("-" * 90)
    print("katso - Katso kaikki pelaajat")
    print("yksi - Katso yksi pelaaja")
    print("lisaa - Lisää pelaaja")
    print("muokkaa - Muokkaa pelaajaa")
    print("poista - Poista pelaaja")
    print("exit - Takaisin päävalikkoon")
    print("-" * 90)

def display_joukkueet():
    print("KOMENTOVALIKKO (JOUKKUEET)")
    print("-" * 90)
    print("katso - Katso kaikki joukkueet")
    print("yksi - Katso yksi joukkue")
    print("lisaa - Lisää joukkue")
    print("muokkaa - Muokkaa joukkuetta")
    print("poista - Poista joukkue")
    print("exit - Takaisin päävalikkoon")
    print("-" * 90)

def display_ottelut():
    print("KOMENTOVALIKKO (OTTELUT)")
    print("-" * 90)
    print("katso - Katso kaikki ottelut")
    print("lisaa - Lisää ottelu")
    print("muokkaa - Muokkaa ottelua")
    print("poista - Poista ottelu")
    print("exit - Takaisin päävalikkoon")
    print("-" * 90)

# Funktio Joukkueet valikossa poistumiseen
def exit_joukkue():
    print("")
    display_joukkueet()
    print("")
    return True

# Funktio Pelaajat valikossa poistumiseen
def exit_pelaajat():
    print("")
    display_pelaajat()
    print("")
    return True

def main():
    db.connect()

    kirjautuminen()

    alku_valinta()

    while True:
        valinta = input("Anna komento: ")
        print("")
        if valinta == '1':
            display_pelaajat()
            while True:
                command = input("Anna komento: ")
                if command == "katso":
                    katso_pelaajat()
                elif command == "yksi":
                    yksi_pelaaja()
                elif command == "lisaa":
                    lisaa_pelaaja()
                elif command == "muokkaa":
                    paivita_pelaaja()
                elif command == "poista":
                    poista_pelaaja()
                elif command == "exit":
                    alku_valinta()
                    break
                else:
                    print("Ei ole komento, syötä uudelleen.\n")
                    display_pelaajat()
        elif valinta == '2':
            display_joukkueet()
            while True:
                command = input("Anna komento: ")
                if command == "katso":
                    katso_joukkueet()
                elif command == "yksi":
                    yksi_joukkue()
                elif command == "lisaa":
                    lisaa_joukkue()
                elif command == "muokkaa":
                    paivita_joukkue()
                elif command == "poista":
                    poista_joukkue()
                elif command == "exit":
                    alku_valinta()
                    break
                else:
                    print("Ei ole komento, syötä uudelleen.\n")
                    display_joukkueet()
        elif valinta == '3':
            display_ottelut()
            while True:
                command = input("Anna komento: ")
                if command == "katso":
                    nayta_ottelut()
                elif command == "lisaa":
                    lisaa_ottelu()
                elif command == "muokkaa":
                    muokkaa_ottelua()
                elif command == "poista":
                    poista_ottelu()
                elif command == "exit":
                    alku_valinta()
                    break
                else:
                    print("Ei ole komento, syötä uudelleen.\n")
                    display_ottelut()
        elif valinta == "exit":
            break
        else:
            print("Väärä valinta, syötä uudelleen\n")
            alku_valinta()

    db.close()
    print("Ohjelma lopetettu.")


# Katso kaikki pelaajat
def katso_pelaajat():
    print("")
    print("Turnaukseen osallistuvat pelaajat\n")
    print("-" * 90)
    line_format = "{:5s} {:25s} {:25s} {:15s}"
    print(line_format.format("ID", "Nimi", "Joukkue", "Rooli"))
    print("-" * 90)
    pelaajat = db.hae_pelaajat()
    for pelaaja in pelaajat:
        print(line_format.format(str(pelaaja.pelaajaID), pelaaja.nimi, pelaaja.joukkueennimi, pelaaja.rooli))
        print("-" * 90)

# Katso kaikki joukkueet
def katso_joukkueet():
    print("")
    print("Turnaukseen osallistuvat joukkueet\n")
    print("-" * 90)
    line_format = "{:5s} {:30s} {:15s} {:20s} {:15s}"
    print(line_format.format("ID", "Nimi", "Paikkakunta", "Päästetyt maalit", "Tehdyt maalit"))
    print("-" * 90)
    joukkueet = db.hae_joukkueet()
    for joukkue in joukkueet:
        print(line_format.format(str(joukkue.joukkueID), joukkue.joukkueennimi, joukkue.paikkakunta, str(joukkue.paastetyt), str(joukkue.tehdyt)))
        print("-" * 90)

# Katso yksi pelaaja
def yksi_pelaaja():
    
    while True:
        print("")
        print("exit - Palaa Pelaajat-valikkoon")
        print("-" * 90)
        try:
            pelaajaID = input("Anna pelaajan ID: ")
            if (pelaajaID == "exit"):
                if exit_pelaajat():
                    break
            pelaajaID = int(pelaajaID)
            print("")
            print("Yksi pelaaja")
            print("-" * 90)
            line_format = "{:5s} {:25s} {:25s} {:15s}"
            print(line_format.format("ID", "Nimi", "Joukkue", "Pelipaikka"))
            print("-" * 90)
            pelaaja = db.hae_pelaaja(pelaajaID)
            print(line_format.format(str(pelaaja.pelaajaID), pelaaja.nimi, pelaaja.joukkueennimi, pelaaja.rooli))
            print("-" * 90)
            print("")
        except Exception as e:
            print("Virhe:", e)
            print("")

# Katso yhden joukkueen pelaajat
def yksi_joukkue():
    print("")

    while True:
        try:
            print("exit - Takaisin Joukkueet-valikkoon")
            print("-" * 90)
            joukkueID = input("Anna joukkueen ID: ")
            if (joukkueID == "exit"):
                if exit_joukkue():
                    break
            joukkueID = int(joukkueID) # input str to int
            print("")
            print("Yksi joukkue")
            print("-" * 90)
            line_format = "{:5s} {:25s}"
            print(line_format.format("ID", "Joukkue"))
            print("-" * 90)
            joukkue = db.hae_joukkue(joukkueID)
            print(line_format.format(str(joukkue.joukkueID), joukkue.joukkueennimi))
            print("-" * 90)
            # Pelaajat
            line_format2 = "{:5s} {:25s} {:15s}"
            print(line_format2.format("ID", "Nimi", "Pelipaikka"))
            print("-" * 90)
            pelaajat = db.kaikki_pelaajat_joukkueesta(joukkueID)
            for pelaaja in pelaajat:
                print(line_format2.format(str(pelaaja.pelaajaID), pelaaja.nimi, pelaaja.rooli))
            print("-" * 90)
            print("")
        except Exception as e:
            print("Virhe:", e)
            print("")

# Lisätään pelaaja
def lisaa_pelaaja():

    while True:
        print("")
        print("exit - Takaisin pelaajat valikkoon")
        print("-" * 90)
        try:
            nimi = input("Nimi: ")
            if (nimi == "exit"):
                if exit_pelaajat():
                    break
            print("Minkä joukkueen pelaaja?")
            print("")
            line_format = "{:5s} {:25s} {:15s} {:15s}"
            print(line_format.format("ID", "Nimi", "Tehdyt maalit", "Päästetyt maalit"))
            joukkueet = db.hae_joukkueet()
            for joukkue in joukkueet:
                print(line_format.format(str(joukkue.joukkueID), joukkue.joukkueennimi, str(joukkue.tehdyt), str(joukkue.paastetyt)))
                print("-" * 90)
            while True:
                print("")
                try:
                    joukkueID = int(input("Valitse joukkueen ID: "))
                    joukkue = db.hae_joukkue(joukkueID) # looks for joukkueID in database
                    break
                except Exception as e:
                    print("Virhe:", e)
            
            while True:
                print("")
                try:
                    pelipaikkaID = int(input("Pelipaikka: 1=Maalivahti, 2=Puolustaja, 3=Hyökkääjä, 4=Huoltaja, 5=Päävalmentaja, 6=Apuvalmentaja, 7=Joukkueenjohtaja: "))
                    db.pelipaikka_error(pelipaikkaID) # Check if the pelipaikkaID is valid
                    break
                except Exception as e:
                    print("Virhe:", e)

            pelaaja = Pelaaja(nimi=nimi, joukkueID=joukkueID, pelipaikkaID=pelipaikkaID)
            db.lisaa_pelaaja(pelaaja)
            print("Uusi pelaaja lisätty onnistuneesti!")
        except Exception as e:
            print("Virhe:", e)
            print("")

# Lisätään joukkue
def lisaa_joukkue():

    while True:
        print("")
        print("exit - Takaisin Joukkueet-valikkoon")
        print("-" * 90)
        try:
            joukkueennimi = input("Joukkueen nimi: ")
            if (joukkueennimi == "exit"):
                if exit_joukkue():
                    break
            paikkakunta = input("Joukkueen kotikaupunki: ")
            if (paikkakunta == "exit"):
                if exit_joukkue():
                    break
            paastetyt = input("Anna päästetyt maalit: ")
            if (paastetyt == "exit"):
                if exit_joukkue():
                    break
            paastetyt = int(paastetyt) # convert str to int
            tehdyt = input("Anna tehdyt maalit: ")
            if (tehdyt == "exit"):
                if exit_joukkue():
                    break
            tehdyt = int(tehdyt) # convert str to int

            joukkue = Joukkue(joukkueennimi=joukkueennimi, paikkakunta=paikkakunta, paastetyt=paastetyt, tehdyt=tehdyt)
            db.lisaa_joukkue(joukkue)
            print("Joukkue lisätty onnistuneesti!")
            print("")
            break
        except Exception as e:
            print("Virhe joukkuetta lisätessä:", e)
            print("Joukkuetta ei lisätty.")

# Päivitetään pelaajan tiedot
def paivita_pelaaja():

    while True:
        print("")
        print("exit - Takaisin Pelaajat-valikkoon")
        print("-" * 90)
        try:
            pelaajaID = input("Syötä pelaajan ID: ")
            if (pelaajaID == "exit"):
                if exit_pelaajat():
                    break
            pelaajaID = int(pelaajaID)
            choice = input("Oletko varma? (k/e): ")
            if (choice == "k"):
                pelipaikkaID = input("Pelipaikka: (1=Maalivahti, 2=Puolustaja, 3=Hyökkääjä, 4=Huoltaja, 5=Päävalmentaja, 6=Apuvalmentaja, 7=Joukkueenjohtaja): ")
                db.paivita_pelipaikka(pelaajaID, pelipaikkaID)
                print(f"Pelaajan {pelaajaID} status päivitetty.")
            else:
                print("Pelaajan päivitys epäonnistui.")
        except Exception as e:
            print("Virhe: ", e)


# Päivitetään joukkueen tiedot
def paivita_joukkue():
    
    while True:
        print("exit - Takaisin Joukkueet-valikkoon")
        print("-" * 90)
        try:
            joukkueID = input("Syötä joukkueen ID: ")
            if (joukkueID == "exit"):
                if exit_joukkue():
                    break
            joukkueID = int(joukkueID)  # muutetaan input intiksi
            joukkueennimi = input("Syötä joukkueen nimi: ")
            if (joukkueennimi == "exit"): 
                if exit_joukkue(): # the nested exit_joukkue() function is called and if it returns True, the while loop is exited with the break statement.
                    break
            paikkakunta = input("Joukkueen paikkakunta: ")
            if (paikkakunta == "exit"):
                if exit_joukkue():
                    break
            paastetyt = input("Syötä päästetyt maalit: ")
            if (paastetyt == "exit"):
                if exit_joukkue():
                    break
            paastetyt = int(paastetyt) # muutetaan input intiksi
            tehdyt = input("Syötä tehdyt maalit: ")
            if (tehdyt == "exit"):
                if exit_joukkue():
                    break
            tehdyt = int(tehdyt) # muutetaan input intiksi
            db.paivita_joukkue(joukkueID, joukkueennimi, paikkakunta, paastetyt, tehdyt)
            print(f"Joukkueen {joukkueID} tiedot on päivitetty!")
            display_joukkueet()
            print("")
            break
        except Exception as e:
            print("")
            print("Virhe päivitettäessä joukkuetta:", e)
            print("Tietoja ei päivitetty.")
            print("")
    
# Poistetaan pelaaja
def poista_pelaaja():
    print("")
    while True:
        print("exit - Takaisin Pelaajat-valikkoon")
        print("-" * 90)
        try:
            pelaajaID = input("Pelaajan ID: ")
            if (pelaajaID == "exit"):
                if exit_pelaajat():
                    break
            pelaajaID = int(pelaajaID)
            pelaaja = db.hae_pelaaja(pelaajaID)
            choice = input("Oletko varma, että haluat poistaa '" + pelaaja.nimi + "'? (k/e): ")
            if (choice == "k"):
                db.poista_pelaaja(pelaajaID)
                print("'" + pelaaja.nimi + "' poistettiin onnistuneesti!\n")
            else:
                print("Pelaajan poistaminen epäonnistui.")
                print("")
        except Exception as e:
            print("Virhe: ", e)
            print("")

# Poistetaan joukkue
def poista_joukkue():

    while True:
        print("exit - Takaisin Joukkueet-valikkoon")
        print("-" * 90)
        try:
            joukkueID = input("Joukkueen ID: ")
            if (joukkueID == "exit"):
                if exit_joukkue():
                    break
            joukkueID = int(joukkueID)
            joukkue = db.hae_joukkue(joukkueID)
            choice = input("Oletko varma, että haluat poistaa '" + joukkue.joukkueennimi + "'? (k/e): ")
            if (choice == "k"):
                db.poista_joukkue(joukkueID)
                print("'" + joukkue.joukkueennimi + "' poistettiin onnistuneesti!\n")
                break
            else:
                print("Joukkueen poistaminen epäonnistui.")
                print("")
        except Exception as e:
            print("Virhe:", e)
            print("")

# Näytä kaikki ottelut
def nayta_ottelut():
    print("")
    print("Turnauksen ottelut\n")
    print("-" * 90)
    line_format = "{:5s} {:25s} {:25s} {:15s}"
    print(line_format.format("ID", "kotijoukkue", "vierasjoukkue", "aloitusaika"))
    print("-" * 90)
    ottelut = db.kaikki_ottelut()
    for ottelu in ottelut:
        aloitusaika_str = ottelu.aloitusaika.strftime("%Y-%m-%d %H:%M")
        print(line_format.format(str(ottelu.peliID), str(ottelu.kotijoukkue), str(ottelu.vierasjoukkue), aloitusaika_str))
        print("-" * 90)
    print("")

# Lisää ottelu
def lisaa_ottelu():
    while True:
        try:
            while True:
                try:
                    kotijoukkueID = int(input("Kotijoukkueen ID: "))
                    db.hae_joukkue(kotijoukkueID) # checks if team exists in database
                    break
                except Exception as e:
                    print("Virhe: ", e)
                    print("")

            while True:
                try:
                    vierasjoukkueID = int(input("Vierasjoukkueen ID: "))
                    db.hae_joukkue(vierasjoukkueID)
                    break
                except Exception as e:
                    print("Virhe: ", e)
                    print("")

            aloitusaika_str = input("Aloitusaika (YYYY-MM-DD HH:MM:SS): ")
            aloitusaika = datetime.datetime.strptime(aloitusaika_str, '%Y-%m-%d %H:%M:%S')

            ottelu = Ottelu(kotijoukkue=kotijoukkueID, vierasjoukkue=vierasjoukkueID, aloitusaika=aloitusaika)
            db.lisaa_ottelu(ottelu)
            print("Ottelu lisätty onnistuneesti!")
            print("")
            break

        except Exception as e:
            print("Virhe lisätessä ottelua:", e)
            print("")

# Muokkaa ottelua
def muokkaa_ottelua():
    while True:
        try:
            while True:
                try:
                    peliID = int(input("Syötä muokattavan ottelun ID: "))
                    db.hae_ottelu(peliID)
                    break
                except Exception as e:
                    print("Virhe: ", e)
                    print("")
            
            while True:
                try:
                    kotijoukkue = int(input("Syötä kotijoukkueen ID: "))
                    db.hae_joukkue(kotijoukkue)
                    break
                except Exception as e:
                    print("Virhe: ", e)
                    print("")

            while True:
                try:
                    vierasjoukkue = int(input("Syötä vierasjoukkueen ID: "))
                    db.hae_joukkue(vierasjoukkue)
                    break
                except Exception as e:
                    print("Virhe: ", e)
                    print("")


            aloitusaika_str = input("Syötä uusi aloitusaika (YYYY-MM-DD HH:MM:SS): ")
            aloitusaika = datetime.datetime.strptime(aloitusaika_str, '%Y-%m-%d %H:%M:%S')
            db.paivita_ottelu(peliID, kotijoukkue, vierasjoukkue, aloitusaika)
            print(f"Ottelun {peliID} tiedot päivitetty!")
            print("")
            break
        except Exception as e:
            print("Ottelun päivittäminen epäonnistui:", e)
            print("")
            break

# Poista ottelu
def poista_ottelu():
    while True:
        try:
            while True:
                try:
                    peliID = int(input("Syötä poistettavan ottelun ID: "))
                    ottelu = db.hae_ottelu(peliID)
                    break
                except Exception as e:
                    print("Virhe: ", e)
                    print("")

            choice = input("Oletko varma, että haluat poistaa ottelun '" + str(ottelu.peliID) + "'? (k/e) ")
            if (choice == "k"):
                db.poista_ottelu(peliID)
                print("Ottelu ID '" + str(ottelu.peliID) + "' poistettiin onnistuneesti!")
                print("")
                break
            else:
                print("Ottelun poistaminen epäonnistui.")
                print("")
                break

        except TypeError as e:
            print("Virhe: ", e)

if __name__ == "__main__":
    main()