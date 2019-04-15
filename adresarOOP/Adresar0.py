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
        return("Osoba - {} {} adresa({}), kontakt({}), štítky({})".format(self.jmeno,self.prijmeni,self.adresa(),self.kontakt(),self.stitek()))
        pass

    def __repr__(self):
        return(str(self))
        pass

    def adresa(self, bydliste=None, obec=None, psc=None):
        """ nastaví nebo vrátí adresu """
        if(bydliste == None and obec == None and psc == None):
            return([self.bydliste, self.obec, self.psc])
        else:
            self.bydliste = bydliste
            self.obec = obec
            self.psc = psc

        pass

    def kontakt(self, mail=None, mobil=None):
        """ nastaví nebo vrátí kontakt"""
        if(mail == None and mobil == None):
            return([self.mail, self.mobil])
        else:
            self.mail = mail
            self.mobil = mobil
            
        pass

    def pridej_stitek(self, stitek):
        """ přidá štítek do seznamu """
        self.stitky.append(stitek)
        
        pass

    def stitek(self, stitek=None):
        """
        vrátí  True ne bo False, zda štítek je nebo není nastaven 
        pokud je sitek=None - vrátí seznam všech štítků
        """

        if(stitek == None):
            return(self.stitky)
        else:
            return(stitek in self.stitky)
        pass

class Adresar:
    """ adresář """
    def __init__(self):
        self.adresy = []

    def pridej(self, osoba):
        """ přidá osoba do adresáře """
        self.adresy.append(osoba)
        pass

    def __str__(self):
        sss = ""

        for i in self.adresy:
            sss += str(i) + "\n"
        
        return sss
         
    def __repr__(self):
        return(str(self))
        pass
    
    def __iadd__(self, other):
        """ přidání kontaktu do adresáře pomocí += """
        self.adresy.append(other)
        pass

    def __iter__(self):
        return iter(self.adresy)
        pass

    def __next__(self):
        return next(self.adresy)
        pass

if __name__ == "__main__":
    print("ahojda")
    os = Osoba("Marek","Ahoj")
    adresar = Adresar()
    adresar.pridej(os)

    os = Osoba("Strnadová", "Anežka")
    os.adresa("Hradec", "50801", "U Školy")

    adresar.pridej(os)

    print(adresar)
