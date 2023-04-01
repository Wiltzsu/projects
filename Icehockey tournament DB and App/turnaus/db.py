import mysql.connector
from contextlib import closing
from oliot import Pelaaja, Joukkue, Ottelu

server = "localhost"
database = "turnaus"
username = "root"
password = ""

mydb = None

def connect():
    global mydb
    if not mydb:
        mydb = mysql.connector.connect(host=server, database=database, user=username, passwd=password)
        mydb.row_factory = mysql.connector.ROWID

def close():
    if mydb:
        mydb.close()

# Työntekijä kirjautuminen
def login(nimi, pelipaikkaID):
    query = "SELECT COUNT(*) FROM pelaajat WHERE nimi=%s AND pelipaikkaID=%s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (nimi, pelipaikkaID))
        tulos = cursor.fetchone()
    
    if tulos[0] > 0:
        return True
    else:
        return False

# Luo uusi pelaaja
def luo_pelaaja(rivi):
    return Pelaaja(rivi["pelaajaID"], rivi["nimi"], rivi["joukkueID"], rivi["pelipaikkaID"], rivi["joukkueennimi"], rivi["rooli"])

# Luo uusi joukkue
def luo_joukkue(rivi):
    return Joukkue(rivi["joukkueID"], rivi["joukkueennimi"], rivi["paikkakunta"], rivi["paastetyt"], rivi["tehdyt"])

# Luo uusi ottelu
def luo_ottelu(rivi):
    return Ottelu(rivi["peliID"], rivi["kotijoukkue"], rivi["vierasjoukkue"], rivi["aloitusaika"])

# Hae kaikki pelaajat
def hae_pelaajat():
    query = "SELECT pelaajat.*, joukkueet.joukkueennimi, pelipaikka.rooli FROM pelaajat INNER JOIN joukkueet ON pelaajat.joukkueID = joukkueet.joukkueID INNER JOIN pelipaikka ON pelaajat.pelipaikkaID = pelipaikka.pelipaikkaID ORDER BY pelaajaID"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query)
        tulokset = cursor.fetchall()
    pelaajat = []
    for rivi in tulokset:
        pelaajat.append(luo_pelaaja(rivi))
    return pelaajat

# Hae yksi pelaaja
def hae_pelaaja(pelaajaID):
    # Virheilmoitus mikäli joukkueIDtä ei ole olemassa tietokannassa
    query = "SELECT COUNT(*) FROM pelaajat WHERE pelaajaID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (pelaajaID,))
        result = cursor.fetchone()
    if result[0] == 0:
        raise ValueError("Virheellinen pelaajaID " + "'" + str(pelaajaID) + "'")
    # Pelaajan haku
    query = "SELECT * FROM pelaajat INNER JOIN joukkueet ON pelaajat.joukkueID = joukkueet.joukkueID INNER JOIN pelipaikka ON pelaajat.pelipaikkaID = pelipaikka.pelipaikkaID WHERE pelaajaID = %s"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query, (pelaajaID,))
        tulokset = cursor.fetchone()
    pelaaja = luo_pelaaja(tulokset)
    return pelaaja

# Hae kaikki pelaajat yhdestä joukkueesta
def kaikki_pelaajat_joukkueesta(joukkueID):
    query = "SELECT pelaajat.*, joukkueet.joukkueennimi, pelipaikka.rooli FROM pelaajat INNER JOIN joukkueet ON pelaajat.joukkueID = joukkueet.joukkueID INNER JOIN pelipaikka ON pelaajat.pelipaikkaID = pelipaikka.pelipaikkaID WHERE pelaajat.joukkueID = %s ORDER BY rooli"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query, (joukkueID,))
        tulokset = cursor.fetchall()
    pelaajat = []
    for rivi in tulokset:
        pelaajat.append(luo_pelaaja(rivi))
    return pelaajat


# Lisää yksi pelaaja
def lisaa_pelaaja(pelaaja):
    query = "INSERT INTO pelaajat (nimi, joukkueID, pelipaikkaID) VALUES (%s, %s, %s)"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (pelaaja.nimi, pelaaja.joukkueID, pelaaja.pelipaikkaID))
        mydb.commit()

# Pelipaikka error
def pelipaikka_error(pelipaikkaID):
    query = "SELECT COUNT(*) FROM pelipaikka WHERE pelipaikkaID = %s"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query, (pelipaikkaID,))
        result = cursor.fetchone()
        if result['COUNT(*)'] == 0:
            raise ValueError("Virheellinen pelipaikkaID " + "'" + str(pelipaikkaID) + "'")

# Lisää joukkue
def lisaa_joukkue(joukkue):
    query = "INSERT INTO joukkueet (joukkueennimi, paikkakunta, paastetyt, tehdyt) VALUES (%s, %s, %s, %s)"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (joukkue.joukkueennimi, joukkue.paikkakunta, joukkue.paastetyt, joukkue.tehdyt))
        mydb.commit()

# Hae kaikki joukkueet
def hae_joukkueet():
    query = "SELECT * FROM joukkueet"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query)
        tulokset = cursor.fetchall()

    joukkueet = []
    for rivi in tulokset:
        joukkueet.append(luo_joukkue(rivi))
    return joukkueet

# Hae yksi joukkue
def hae_joukkue(joukkueID):
    # Virheilmoitus mikäli joukkueIDtä ei ole olemassa tietokannassa
    query = "SELECT COUNT(*) FROM joukkueet WHERE joukkueID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (joukkueID,))
        result = cursor.fetchone()
        if result[0] == 0:
            raise ValueError("Virheellinen joukkueID " + "'" + str(joukkueID) + "'")
    # Joukkueen haku
    query = "SELECT * FROM joukkueet WHERE joukkueID = %s"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query, (joukkueID,))
        tulokset = cursor.fetchone()
    
    joukkue = luo_joukkue(tulokset)
    return joukkue

# Päivittää pelaajan pelipaikan
def paivita_pelipaikka(pelaajaID, pelipaikkaID):
    query = "SELECT COUNT(*) FROM pelaajat WHERE pelaajaID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (pelaajaID,))
        result = cursor.fetchone()
        if result[0] == 0:
            raise ValueError("Virheellinen pelaajaID " + "'" + str(pelaajaID) + "'")
    
    query = "UPDATE pelaajat SET pelipaikkaID = %s WHERE pelaajaID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (pelipaikkaID, pelaajaID))
        mydb.commit()

# Päivittää joukkueen tiedot
def paivita_joukkue(joukkueID, joukkueennimi, paikkakunta, paastetyt, tehdyt):
    # Virheilmoitus mikäli joukkueIDtä ei ole olemassa tietokannassa
    query = "SELECT COUNT(*) FROM joukkueet WHERE joukkueID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (joukkueID,))
        result = cursor.fetchone()
        if result[0] == 0:
            raise ValueError("Virheellinen joukkueID " + "'" + str(joukkueID) + "'")
    # Päivitys
    query = "UPDATE joukkueet SET joukkueennimi = %s, paikkakunta = %s, paastetyt = %s, tehdyt = %s WHERE joukkueID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (joukkueennimi, paikkakunta, paastetyt, tehdyt, joukkueID))
        mydb.commit()

# Poistaa pelaajan
def poista_pelaaja(pelaajaID):
    # Virheilmoitus mikäli joukkueIDtä ei ole olemassa tietokannassa
    query = "SELECT COUNT(*) FROM pelaajat WHERE pelaajaID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (pelaajaID,))
        result = cursor.fetchone()
        if result[0] == 0:
            raise ValueError("Virheellinen pelaajaID " + "'" + str(pelaajaID) + "'")

    query = "DELETE FROM pelaajat WHERE pelaajaID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (pelaajaID,))
        mydb.commit()

# Poistaa joukkueen
def poista_joukkue(joukkueID):
    query = "DELETE FROM joukkueet WHERE joukkueID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (joukkueID,))
        mydb.commit()

# Hae kaikki ottelut
def kaikki_ottelut():
    query = "SELECT pelit.peliID, kotijoukkue.joukkueennimi AS kotijoukkue, vierasjoukkue.joukkueennimi AS vierasjoukkue, pelit.aloitusaika FROM pelit JOIN joukkueet AS kotijoukkue ON pelit.kotijoukkue = kotijoukkue.joukkueID JOIN joukkueet AS vierasjoukkue ON pelit.vierasjoukkue = vierasjoukkue.joukkueID ORDER BY aloitusaika ASC;"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query)
        tulokset = cursor.fetchall()
    ottelut = []
    for rivi in tulokset:
        ottelut.append(luo_ottelu(rivi))
    return ottelut

# Lisää ottelu
def lisaa_ottelu(ottelu):
    query = "INSERT INTO pelit (kotijoukkue, vierasjoukkue, aloitusaika) VALUES (%s, %s, %s)"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (ottelu.kotijoukkue, ottelu.vierasjoukkue, ottelu.aloitusaika))
        mydb.commit()

# Päivitä ottelu
def paivita_ottelu(peliID, kotijoukkue, vierasjoukkue, aloitusaika):
    query = "UPDATE pelit SET kotijoukkue = %s, vierasjoukkue = %s, aloitusaika = %s WHERE peliID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (kotijoukkue, vierasjoukkue, aloitusaika, peliID))
        mydb.commit()

# Hae ottelu
def hae_ottelu(peliID):
    # Virheilmoitus mikäli peliIDtä ei ole olemassa tietokannassa
    query = "SELECT COUNT(*) FROM pelit WHERE peliID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (peliID,))
        result = cursor.fetchone()
        if result[0] == 0:
            raise ValueError("Virheellinen peliID " + "'" + str(peliID) + "'")

    query = "SELECT * FROM pelit WHERE peliID = %s"
    with closing(mydb.cursor(dictionary=True)) as cursor:
        cursor.execute(query, (peliID,))
        tulokset = cursor.fetchone()
    ottelu = luo_ottelu(tulokset)
    return ottelu

# Poista ottelu 
def poista_ottelu(peliID):
    query = "DELETE FROM pelit WHERE peliID = %s"
    with closing(mydb.cursor()) as cursor:
        cursor.execute(query, (peliID,))
        mydb.commit()