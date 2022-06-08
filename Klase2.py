# -*- coding: utf-8 -*-
"""
Created on Tue May 31 08:43:31 2022

@author: Marija Gijic
"""
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
            format_linije.format("Datum rodjenja", datetime.strptime(self.__datum_rodjenja, "%d-%m-%Y").date()),
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
        self.__digitalni_sertifikat = []
        self.__primljene_doze = []
        self.__potvrde_o_izvrsenoj_vakcinaciji = []
        
    
    
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
    @zdravstvena_ustanova.setter 
    def zdravstvena_ustanova(self, zdravstvena_ustanova):
        self.__zdravstvena_ustanova = zdravstvena_ustanova
        
    def __init__(self, jmbg, ime, prezime, datum_rodjenja, pol, zdravstvena_ustanova):
        super().__init__(jmbg, ime, prezime, datum_rodjenja, pol)
        self.__zdravstvena_ustanova = zdravstvena_ustanova

class Doza:
    @property
    def datum_vakcinacije(self):
        return self.__datum_vakcinacije
    @datum_vakcinacije.setter 
    def datum_vakcinacije(self, datum_vakcinacije):
        self.__datum_vakcinacije = datum_vakcinacije
        
    @property 
    def vakcina(self):
        return self.__vakcina
    @vakcina.setter
    def vakcina(self, vakcina):
        self.__vakcina = vakcina
        
    @property
    def zdravstveni_radnik(self):
        return self.__zdravstveni_radnik
    
    @property 
    def zemlja(self):
        return self.__zemlja
    @zemlja.setter 
    def zemlja(self, zemlja):
        self.__zemlja = zemlja
        
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
            format_linije.format("Datum vakcinacije",datetime.strptime(self.__datum_vakcinacije, "%d-%m-%Y").date()),
            format_linije.format("Vakcina", self.__vakcina.naziv),
            format_linije.format("Zdravstveni radnik", "{}: {} {}".format("Ime i prezime", self.__zdravstveni_radnik.ime, self.__zdravstveni_radnik.prezime )),
            format_linije.format("Zemlja", self.__zemlja),
            format_linije.format("Gradjanin", "{}: {} {}".format("Ime i prezime", self.__gradjanin.ime, self.__gradjanin.prezime))
            ])
        
    def sadrzi(self, gradjanin):
        return gradjanin in self.__gradjanin
    
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
    @serijski_broj.setter 
    def serijski_broj(self, serijski_broj):
        self.__serijski_broj = serijski_broj
        
    @property
    def zemlja_porekla(self):
        return self.__zemlja_porekla #bar dva karaktera
    @zemlja_porekla.setter 
    def zemlja_porekla(self, zemlja_porekla):
        self.__zemlja_porekla = zemlja_porekla
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
            format_linije.format("Rok trajanja", datetime.strptime(self.__rok_trajanja, "%d-%m-%Y").date())
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

    def sadrzi(self, gradjanin):
        return gradjanin in self.__gradjanin
    
    
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
    
    def __init__(self, sifra_sertifikata, datum_izdavanja_sertifikata, gradjanin):
        self.__sifra_sertifikata = sifra_sertifikata
        self.__datum_izdavanja_sertifikata = datum_izdavanja_sertifikata
        self.__gradjanin = gradjanin
    
    def __str__(self):
        return "\n".join ([
            "",
            "{:>10}: {}".format("Sifra seritifikata", self.__sifra_sertifikata),
            "{:>10}: {}".format("Datum izdavanja", datetime.strptime(self.__datum_izdavanja_sertifikata, "%d-%m-%Y").date()),
            "{:>1o}: {}".format("Gradjanin", "{} {}".format(self.__gradjanin.ime, self.__gradjanin.prezime))
            ])
    def sadrzi(self, gradjanin):
        return gradjanin in self.__gradjanin
    
class Podaci:
    
    @property 
    def lista_gradjana(self):
        return self.__lista_gradjana
    @property 
    def zdravstveni_radnici(self):
        return self.__zdravstveni_radnici
   
    def __init__(self):
        self.__lista_gradjana = []
        self.__zdravstveni_radnici = []
      
    
        
    @classmethod 
    def napravi_pocetne(cls):
        podaci = Podaci()
        lista_gradjana = podaci.lista_gradjana
        lista_gradjana.append(Gradjanin("121213121", "Marko", "Matic", "3-3-2002", "m", "13124232424"))
        lista_gradjana.append(Gradjanin("1212323221", "Ana", "Miric", "2-3-2000", "z", "132131231123"))
        lista_gradjana.append(Gradjanin("13211312321", "Slavko", "Suzic", "3-12-2001", "m", "21224232424"))
        zdravstveni_radnici = podaci.zdravstveni_radnici
        zdravstveni_radnici.append(ZdravstveniRadnik("12313132", "Mirko", "Savic", "2-2-1998", "m", "Bolnica"))
        Gradjanin.dodaj_primljene_doze(lista_gradjana[0],Doza("4-3-2021", 
                                            "Fajzer",
                                            zdravstveni_radnici[0],
                                            "Nemacka",
                                            lista_gradjana[0]))
        Gradjanin.dodaj_primljene_doze(lista_gradjana[1],Doza("4-3-2021", 
                                            "Fajzer",
                                            zdravstveni_radnici[0],
                                            "Madjarska",
                                            lista_gradjana[1]))
        Gradjanin.dodaj_primljene_doze(lista_gradjana[2],Doza("4-3-2021", 
                                            "Fajzer",
                                            zdravstveni_radnici[0],
                                            "Nemacka",
                                            lista_gradjana[2]))
        
       
        Gradjanin.dodaj_potvrde_o_izvrsenoj_vakcinaciji(lista_gradjana[0], PotvrdaOIzvrsenojVakcinaciji("123132123132",
                                                                                                       "12-3-2021", 
                                                                                                       Doza("4-3-2021", "Fajzer", zdravstveni_radnici[0], 
                                                                                                            "Nemacka", lista_gradjana[0]), 
                                                                                                       lista_gradjana[0], 
                                                                                                       zdravstveni_radnici[0]))
        Gradjanin.dodaj_digitalni_sertifikat(lista_gradjana[0], DigitalniSertifikat("123123123132", "12-3-2021", lista_gradjana[0]))
        
        return podaci
    
    __datoteka = "podaci_gradjani"
    
    @classmethod 
    def sacuvaj(cls, podaci):
        datoteka = open(cls.__datoteka, "wb")
        pickle.dump(podaci, datoteka)
        datoteka.close()
        
        
    @classmethod
    def ucitaj(cls):
        try:
            datoteka = open(cls.__datoteka, "rb")
            podaci = pickle.load(datoteka)
            datoteka.close()
        except FileNotFoundError:  
            return Podaci.napravi_pocetne()  

        return podaci
    
    
    def pronadji_gradjanina(self,  jmbg):
        for gradjanin in self.__lista_gradjana:
            if gradjanin.jmbg == jmbg:
                return gradjanin

    def dodaj_gradjana(self, gradjanin):
        self.__lista_gradjana.append(gradjanin)

    def obrisi_proizvod(self, indeks):
        gradjanin = self.__lista_proizvoda.pop(indeks)

        doze_za_brisanje = []
        potvrde_za_brisanje = []
        digitalni_sertifikat_za_brisanje = []
        for doza in Gradjanin.primljene_doze:
            if doza.sadrzi(gradjanin):
                doze_za_brisanje.append(doza)
        for doza in doze_za_brisanje:
            Gradjanin.primljene_doze.remove(doza)
                
        for potvrda in Gradjanin.potvrde_o_izvrsenoj_vakcinaciji:
            if potvrda.sadrzi(gradjanin):
                potvrde_za_brisanje.append(potvrda)
        
        for potvrda in potvrde_za_brisanje:
            Gradjanin.potvrde_o_izvrsenoj_vakcinaciji.remove(potvrda)
                
        for sertifikat in Gradjanin.digitalni_sertifikat:
            if sertifikat.sadrzi(gradjanin):
                digitalni_sertifikat_za_brisanje.append(sertifikat)
        for sertifikat in digitalni_sertifikat_za_brisanje:
            Gradjanin.digitalni_sertifikat.remove(sertifikat)
