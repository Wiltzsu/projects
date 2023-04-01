
class Pelaaja:
    def __init__(self, pelaajaID=0, nimi=None, joukkueID=0, pelipaikkaID=0, joukkueennimi=None, rooli=None):
        self.pelaajaID = pelaajaID
        self.nimi = nimi
        self.joukkueID = joukkueID
        self.pelipaikkaID = pelipaikkaID
        self.joukkueennimi = joukkueennimi
        self.rooli = rooli
        
class Joukkue:
    def __init__(self, joukkueID=0, joukkueennimi=None, paikkakunta=None, paastetyt=0, tehdyt=0):
        self.joukkueID = joukkueID
        self.joukkueennimi = joukkueennimi
        self.paikkakunta = paikkakunta
        self.paastetyt = paastetyt
        self.tehdyt = tehdyt

class Ottelu:
    def __init__(self, peliID=0, kotijoukkue=None, vierasjoukkue=None, aloitusaika=0, joukkueennimi=None):
        self.peliID = peliID
        self.kotijoukkue = kotijoukkue
        self.vierasjoukkue = vierasjoukkue
        self.aloitusaika = aloitusaika
        self.joukkueennimi = joukkueennimi