#import uuid
from datetime import datetime
#from datetime import date
import pickle

class Osoba:
    @property
    def jmbg(self):
        return self.__jmbg #mora da ima 13 karaktera, jedinstven
    @jmbg.setter 
    def jmbg(self, jmbg):
        self.__jmbg = jmbg
    @property
    def ime(self):
        return self.__ime  #tipa string, najmanje 2 karaktera
    @ime.setter
    def ime(self, ime):
        self.__ime = ime
    @property
    def prezime(self):
        return self.__prezime  #tipa string, najmanje 2 karaktera
    @prezime.setter 
    def prezime(self, prezime):
        self.__prezime = prezime
    @property 
    def datum_rodjenja(self):
        return self.__datum_rodjenja #tip date, najkasnije tekuci datum
    @datum_rodjenja.setter 
    def datum_rodjenja(self, datum_rodjenja):
        self.__datum_rodjenja = datum_rodjenja
    @property 
    def pol(self):
        return self.__pol #tipa string, muski/zenski
    @pol.setter
    def pol(self, pol):
        self.__pol = pol
        
        
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol):
        self.__jmbg = jmbg
        self.__ime = ime
        self.__prezime = prezime
        self.__datum_rodjenja = datum_rodjenja
        self.__pol = pol
        
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Jmbg", self.__jmbg),
            format_linije.format("Ime", self.__ime),
            format_linije.format("Prezime", self.__prezime),
            format_linije.format("Datum rodjenja", datetime.strptime(self.__datum_rodjenja, "%Y-%m-%d").date()),
            format_linije.format("Pol", self.__pol)
    
            
            ])

class Gradjanin(Osoba):
    @property
    def broj_licne_karte(self):
        return self.__broj_licne_karte #10 karaktera, jedinstven
    @broj_licne_karte.setter 
    def broj_licne_karte(self, broj_licne_karte):
        self.__broj_licne_karte = broj_licne_karte
    @property 
    def primljene_doze(self): #lista primljenih doza
        return self.__primljene_doze
    
    @property 
    def potvrde_o_izvrsenoj_vakcinaciji(self):
        return self.__potvrde_o_izvrsenoj_vakcinaciji #lista potvrda o izvrsenoj vakc.
    @property 
    def digitalni_sertifikat(self): 
        return self.__digitalni_sertifikat
    
    
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol, broj_licne_karte):
        super().__init__(jmbg, ime, prezime, datum_rodjenja, pol)
        self.__broj_licne_karte = broj_licne_karte
        self.__primljene_doze = []
        self.__potvrde_o_izvrsenoj_vakcinaciji = []
        self.__digitalni_sertifikat = []
        
    def dodaj_primljene_doze(self, doza):
        self.__primljene_doze.append(doza)
    
    def dodaj_potvrde_o_izvrsenoj_vakcinaciji(self, potvrda_o_izvrsenoj_vakcinaciji):
        self.__potvrde_o_izvrsenoj_vakcinaciji.append(potvrda_o_izvrsenoj_vakcinaciji)
    
    def dodaj_digitalni_sertifikat(self, digitalni_sertifikat):
        self.__digitalni_sertifikat.append(digitalni_sertifikat)
        
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            super().__str__(),
            format_linije.format("Broj licne", self.__broj_licne_karte),
            format_linije.format("Primljene doze", self.__primljene_doze),
            format_linije.format("Potvrde o izvrsenoj vakcinaciji", self.__potvrde_o_izvrsenoj_vakcinaciji),
            format_linije.format("Digitalni sertifikat", self.__digitalni_sertifikat)
            ])
        
class ZdravstveniRadnik(Osoba):
    @property
    def zdravstvena_ustanova(self):
        return self.__zdravstvena_ustanova
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol, zdravstvena_ustanova):
        super().__init__(jmbg, ime, prezime, datum_rodjenja, pol)
        self.__zdravstvena_ustanova = zdravstvena_ustanova

class Doza:
    @property
    def datum_vakcinacije(self):
        return self.__datum_vakcinacije
    @property 
    def vakcina(self):
        return self.__vakcina
    @property
    def zdravstveni_radnik(self):
        return self.__zdravstveni_radnik
    @property 
    def zemlja(self):
        return self.__zemlja
    @property
    def gradjanin(self):
        return self.__gradjanin
    
    
    def __init__(self, datum_vakcinacije, vakcina, zdravstveni_radnik, zemlja, gradjanin):
        self.__datum_vakcinacije = datum_vakcinacije
        self.__vakcina = vakcina
        self.__zdravstveni_radnik = zdravstveni_radnik
        self.__zemlja = zemlja
        self.__gradjanin = gradjanin
    
    
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Datum vakcinacije", self.__datum_vakcinacije),
            format_linije.format("Vakcina", self.__vakcina.naziv),
            format_linije.format("Zdravstveni radnik", self.__zdravstveni_radnik.ime),
            format_linije.format("Zemlja", self.__zemlja),
            format_linije.format("Gradjanin", self.__gradjanin)
            ])
        
class Vakcina:
    @property 
    def naziv(self):
        return self.__naziv #bar dva karaktera
    @naziv.setter 
    def naziv(self, naziv):
        self.__naziv = naziv
    @property 
    def serijski_broj(self):
        return self.__serijski_broj #10 karaktera, jedinstven
    @property
    def zemlja_porekla(self):
        return self.__zemlja_porekla #bar dva karaktera
    @property
    def rok_trajanja(self):
        return self.__rok_trajanja
    
    def __init__(self, naziv, serijski_broj, zemlja_porekla, rok_trajanja):
        self.__naziv = naziv
        self.__serijski_broj = serijski_broj
        self.__zemlja_porekla = zemlja_porekla
        self.__rok_trajanja = rok_trajanja
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Naziv", self.__naziv),
            format_linije.format("Serijski broj", self.__serijski_broj),
            format_linije.format("Zemlja porekla", self.__zemlja_porekla),
            format_linije.format("Rok trajanja", datetime.strptime(self.__rok_trajanja, "%Y-%m-%d").date())
            ])
    
class PotvrdaOIzvrsenojVakcinaciji:
    @property
    def sifra_potvrde(self):
        return self.__sifra_potvrde
    @property 
    def datum_izdavanja_potvrde(self):
        return self.__datum_izdavanja_potvrde
    @property
    def doza(self):
        return self.__doza
    @property 
    def gradjanin(self):
        return self.__gradjanin
    @property 
    def zdravstveni_radnik(self):
        return self.__zdravstveni_radnik
    
    def __init__(self, sifra_potvrde, datum_izdavanja, doza, gradjanin, zdravstveni_radnik):
        self.__sifra_potvrde = sifra_potvrde
        self.__datum_izdavanja = datum_izdavanja
        self.__doza = doza
        self.__gradjanin = gradjanin
        self.__zdravstveni_radnik = zdravstveni_radnik
    
    def __str__(self):
        format_linije = "{:>10}: {}"
        return "\n".join([
            "",
            format_linije.format("Sifra potvrde", self.__sifra_potvrde),
            format_linije.format("Datum izdavanja", datetime.strptime(self.__datum_izdavanja, "%Y-%m-%d").date()),
            format_linije.format("Doza", self.__doza.naziv),
            format_linije.format("Gradjanin", self.__gradjanin.ime),
            format_linije.format("Zdravstveni radnik", self.__zdravstveni_radnik.ime)
            ])


class DigitalniSertifikat:
    @property 
    def sifra_sertifikata(self):
        return self.__sifra_sertifikata
    @property 
    def datum_izdavanja_sertifikata(self):
        return self.__datum_izdavanja_sertifikata
    @property
    def gradjanin(self):
        return self.__gradjanin
    
    def __init__(self, sifra_sertifikata, datum_izdavanja_sertifikata):
        self.__sifra_sertifikata = sifra_sertifikata
        self.__datum_izdavanja_sertifikata = datum_izdavanja_sertifikata
        self.__gradjanin = []
        
    def dodaj_gradjanina(self, gradjanin):
        self.__gradjanin.append(gradjanin)
