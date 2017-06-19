'''
Created on Jun 18, 2017

@author: Philipp
'''

import random



class Vorlesung:
    def __init__(self,name,tag,cp):
        self.name=name
        self.tag = tag
        self.cp = cp

class Population:
    def __init__(self):
        self.vorlesungen=[]
        self.fitness=0
    
    def addVorlesung(self,VL):
        if VL not in self.vorlesungen:
            self.vorlesungen.append(VL)
            
    def size(self):
        AnzahlKurse=len(self.vorlesungen)
        return AnzahlKurse
    
    def getVorlesung(self, index):
        VL=[index]
        return VL
    

UMO = Vorlesung("UMO","Mittwoch",3)
MethKI = Vorlesung("MethKI","Montag", 6)
WIWIT = Vorlesung("WIWIT","Donnerstag", 6)
PKS = Vorlesung ("PKS","Donnerstag", 6)
EBM = Vorlesung ("EBM","Freitag", 6)
SPIS = Vorlesung("SPIS", "Dienstag", 4)
Englisch = Vorlesung("Englisch", "Mittwoch", 4)
IBIS = Vorlesung ("IBIS", "Dienstag", 6)
SPM = Vorlesung("SPM", "Donnerstag", 6)

MengeVL=[UMO, MethKI, WIWIT, PKS, EBM, SPIS, Englisch, IBIS, SPM]
groesseMengeVL = len(MengeVL)

AnzahlPopulation = int(input("Anzahl der Population:"))
AnzahlKurseSemester = int(input("Anzahl der Kurse in diesem Semester:"))

'''Erzeuge Population'''
Population_dict ={}
CPopulation=0
while len(Population_dict) < AnzahlPopulation:
    
    Population_Neu = Population()
    i=0
    while Population_Neu.size() < AnzahlKurseSemester:
        randomint = random.randint(0,groesseMengeVL-1)
        Population_Neu.addVorlesung(MengeVL[randomint])
        i=i+1
        
    for i in Population_Neu.vorlesungen:
        print(i.name)
    print("Population: " + str(Population_Neu.size()))
    Population_dict[CPopulation]=Population_Neu
    CPopulation= CPopulation +1
    


'''Population1 = [UMO, MethKI, WIWIT, SPIS]
Population2=[IBIS,PKS,EBM, Englisch]'''


freierTag = "Mittwoch"
tagzaehlerPopulation1 = 0
tagzaehlerPopulation2 = 0
sumCP1=0
sumCP2=0
randomint = 0
counter = 0

while True:


    for i in Population1:
        sumCP1 = sumCP1+i.cp
        if i.tag == freierTag:
            tagzaehlerPopulation1=tagzaehlerPopulation1+1
            print(tagzaehlerPopulation1)
            
    for i in Population2:
        sumCP2 = sumCP2+i.cp
        if i.tag == freierTag:
            tagzaehlerPopulation2=tagzaehlerPopulation2+1
            print(tagzaehlerPopulation2)           
    
    if tagzaehlerPopulation1 <=0 and sumCP1>sumCP2:
        print("Deine Vorlesungen P1")
        for i in Population1:
            print(i.name, i.cp, i.tag)
        print(counter)  
        break
    
    elif tagzaehlerPopulation2<=0 and sumCP2>sumCP1:
        print("Deine Vorlesungen P2")
        for i in Population2:
            print(i.name, i.cp, i.tag)
        print(counter)    
        break
    
                  
    '''randomint = random.randint(0,3)'''
    crossoverobjekt1 = Population1[randomint]
    crossoverobjekt2 = Population2[randomint]
    Population1.remove(crossoverobjekt1)
    Population2.remove(crossoverobjekt2)
    
    Population1.append(crossoverobjekt2)
    Population2.append(crossoverobjekt1)
    

    
    counter = counter +1

    tagzaehlerPopulation1 = 0
    tagzaehlerPopulation2 = 0
    sumCP1=0
    sumCP2=0



