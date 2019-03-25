#!/usr/bin/env python3
"""
Osoba    - osoba, její adresa, kontakty, seznam štítků....
Adresar  - seznam kontaktů
"""
class Osoba:
    """ Osoba v adresáři """
    def __init__(self, prijmeni, jmeno):
        self.prijmeni = prijmeni
        self.jmeno = jmeno
        self.bydliste = self.obec = self.psc = self.mail = self.mobil = None
        self.stitky = []

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def adresa(self, bydliste=None, obec=None, psc=None):
        """ nastaví nebo vrátí adresu """
        pass

    def kontakt(self, mail=None, mobil=None):
        """ nastaví nebo vrátí kontakty """
        pass

    def pridej_stitek(self, stitek):
        """ přidá štítek do seznamu """
        pass

    def stitek(self, stitek=None):
        """
        vrátí  True ne bo False, zda štítek je nebo není nastaven 
        pokud je sitek=None - vrátí seznam všech štítků
        """
        pass

class Adresar:
    """ adresář """
    def __init__(self):
        self.adresy = []

    def pridej(osoba):
        """ přidá osoba do adresáře """
        pass

    def __iadd__(self, other):
        """ přidání kontaktu do adresáře pomocí += """
        pass

    def __iter__(self):       
        pass

    def __next__(self):
        pass

