class kubs:
    #metode, kas inicializē objektu
    def __init__(self,garums,krasa):
        if garums>=2 and garums<=10:  
            self.garums=garums
        else:
            print("Malas garums neatbilst nosacījumiem! ")
            self.garums=2
        self.krasa=krasa
        #metode, kas aprekina kuba tilpuma
    def aprekinat_tilpumu(self):
        tilpums=self.garums**3
        return tilpums
        #metode, kas nodzēš objektu
    def __del__(self):
        print("Objekts ir likvidēts! Tā krāsa bija ", self.krasa)

#objekti
kubg = kubs(10,"zaļa")
kubr = kubs(1, "sarkana")
print(kubg.krasa, kubg.aprekinat_tilpumu())
print(kubr.garums)
del kubr
#parbauda vaii eksistē
try:
    print(kubr.garums)
except:
    print("Objekts neeksistē")
print(kubg.garums)

class bloks(kubs):
    def __init__(self, garums, krasa, kubskaits,forma):
        super().__init__(garums,krasa)
        if kubskaits>=1 and kubskaits<=4:
            self.__kubskaits=kubskaits
        else:
            print("Nepareizaz kubu skaita vērtība")
            self.__kubskaits=1
        self.nosaukums=str(krasa)+ str(self.__kubskaits)
        formas_vertibas=[11,12,13,14,22]
        if forma not in formas_vertibas:
            print("Forma neatbilst nosacījumiem")
            self.derigums=0
        else:
            self.derigums=1
    def tilpums(self):
        kuba_tilpums=self.garums**3
        bloka_tilpums= kuba_tilpums*self.__kubskaits
        return bloka_tilpums
    def mainit_form(self,jauna_forma):
        formas_vertibas=[11,12,13,14,22]
        if jauna_forma not in formas_vertibas:
            
            print("Forma neatbilst nosacījumiem")
            self.derigums=0
        else:
            self.derigums=1

#objekti
orange3 = bloks(5,"oranža",3,13)
print(orange3.nosaukums, orange3.tilpums())
zils5=bloks(7,'zila',5,23)
print(zils5.nosaukums,zils5.derigums)
zils5.mainit_form(12)
print(zils5.nosaukums,zils5.derigums)
