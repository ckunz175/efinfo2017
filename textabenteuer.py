

#Erstellen einer Klasse f�r alle R�ume, mit verschiedenen Attributen (diese sind im Moment teilweise noch nicht
#wirklich wichtig, sollen aber Ausbaum�glichkeiten f�r das Programm darstellen)
class Raum:
        def _init_(self,name,boden,pflanzen,objekte,wege,string):
                self.name = name
                self.boden = boden
                self.pflanzen = pflanzen
                self.objekte = objekte
                self.wege = wege
                self.string = string

        def display(self):
                print self.name
                print 50*"-"
                print self.string
                print "Der Boden besteht aus",self.boden
                print "Pflanzen:",self.pflanzen
                print "Du siehst:"
                for obj in self.objekte:
                        print "    ",obj.string
                for direct in self.wege.keys():
                        print "In Richtung",direct,"liegt",self.wege[direct].name

#mit der folgenden Funktion wird gepr�ft, ob beim Betreten eines bestimmten Raumes etwas bestimmtes passiert

def checkEreignis(standort):

        if standort in [bruecke]:
                if spieler.gewicht > 90.0:
                                print "Die Bruecke ist unter deinem Gewicht zusammengebrochen."
                                print "Spiel beendet."
                                return 0


#Als n�chstes die Gehen-Funktion, nochmals aufgeteil in zwei kleinere Funktionen

def goto(standort,ziel):
        if ziel in standort.wege.keys():
                standort = standort.wege[ziel]
                e = checkEreignis(standort)
                if e == 0:
                        return 0
                #wenn die funktion null zur�ckgibt, heisst das, dass das spiel beendet werden soll
                return standort
        else:
                print "\nIn diese Richtung fuehrt kein Weg!\n"
                return standort

def gehe(standortAlt,ziel):
        standort = goto(standortAlt,ziel)
        if standort == 0:
                return 0
        if standort != None:
                        if standort == standortAlt:
                                print "Du bist immer noch hier:",standort.name
                                for direct in standort.wege.keys():
                                        print "In Richtung",direct,"liegt",standort.wege[direct].name
                        else:
                                spieler.standort = standort
                                print "Dein Standort:"
                                standort.display()
                        return standort


#eine verbindung erstellen
def neueVerbindung(ort1,richtung,ort2):
        ort1.wege[richtung] = ort2


#funktion zum Pr�fen des vom Spieler eingegebenen Befehls
def checkBefehl(inp):
        if inp[-1] in ["nehmen"]:
                return "nimm"
        if inp[0] in ["nimm","Nimm"]:
                return "nimm"
        elif inp[0] in ["gehe","Gehe"]:
                return "gehe"
        elif inp[-1] in ["ausr�sten"]:
                return "ausr�sten"

#funktion zum Ermitteln der Richtung (im Falle eines Gehe-Befehls)
def checkRichtung(inp):
        if inp[0] == "Gehe" or "gehe":
                richtung = inp[-1]
                if richtung in ["Norden","n","N","norden"]:
                        return "n"
                if richtung in ["Sueden","s","S","sueden"]:
                        return "s"
                if richtung in ["Osten","o","O","osten"]:
                        return "o"
                if richtung in ["Westen","w","W","westen"]:
                        return "w"
                if richtung in ["Oben","oben","rauf","hinauf"]:
                        return "rauf"
                if richtung in ["Unten","unten","runter","hinunter"]:
                        return "runter"

#Die Klasse Charakter; die Objekte dieser Klasse sind die spieler (man k�nnte noch die m�glichkeit hinzuf�gen, den eigenen charakter in
#einer Datei zu speichern, um ihn sp�ter wieder abzurufen)
class Charakter:
        def _init_(self):
                name = raw_input("Gib deinen Namen ein: ")
                groesse = raw_input("Wie gross bist du?")
                gewicht = raw_input("Wie schwer bist du?")
                self.name = name
                groesse = float(groesse)
                gewicht = float(gewicht)
                self.groesse = groesse
                self.gewicht = gewicht
                self.inventar = []
                self.ausgeruestet = []
                self.standort = None
        def show(self):
                print self.name
                print "Groesse:",self.groesse
                print "Gewicht:",self.gewicht
                print "Inventar:"
                for item in self.inventar:
                        print "    ",item.name
                print "Ausgeruestet:"
                for item in self.ausgeruestet:
                        print "    ",item.name
                print "\n"


#Klasse Objekte: gegenst�nde, die der spieler finden, aufnehmen oder mit denen er interagieren kann
#-> weitere Attribute folgen noch (z.B. der Wert, das Material, spezielle Eigenschaften, usw.)
class Objekt:
        def _init_(self,name,string):
                self.name = name
                self.string = string


#Funktion zum platzieren von objekten an einem bestimmten Ort
def objektPlatzieren(objekt,platz):
        platz.objekte.append(objekt)
        objekt.ort = platz





#Funktion, um objekt von raum in spielerinventar zu verschieben
def objektNehmen(objekt):
        for objekte in spieler.standort.objekte:
                if objekt in [objekte.name,objekte.string]:
                        spieler.inventar.append(objekte)
                        spieler.standort.objekte.remove(objekte)
                        print objekte.string, "aufgenommen"
                else:
                        print "Dieses Objekt gibt es hier nicht./n"

#Funktion, um objekt von inventar noach "ausgeruestet" zu verschieben
def objektAusruesten(objekt):
        for objekte in spieler.inventar:
                if objekte.name == objekt:
                        spieler.ausgeruestet.append(objekte)
                        spieler.inventar.remove(objekte)
                        print objekte.string, "ausgeruestet/n"

#die Shell

def shell(start):
        print "Neuen Charakter erstellen..."
        global spieler
        spieler = Charakter()
        spieler._init_()
        spieler.standort = start
        #-> wie oben schon gesagt k�nnte man sp�ter noch die M�glichkeit einbauen, verschiedene Spielerprofile zu erstellen
        print "Ihr Charakter:"
        spieler.show()
        standort = start
        print "Dein Standort:"
        standort.display()

        while True:
                #input des Spielers
                inp = raw_input(">>")
                if inp == "exit":
                        return
                splitted = inp.split(" ")
                befehl = checkBefehl(splitted)

                #Ausf�hren des Befehls
                if befehl == "gehe":
                        richtung = checkRichtung(splitted)
                        standort = gehe(standort,richtung)
                        if standort == 0:
                                return
                if befehl == "nimm":
                        objektNehmen(splitted[-1])
                        spieler.show()
                if befehl == "ausruesten":
                        objektAusruesten(splitted[0])
                        spieler.show()











#erstellen von R�umen und Verbindungen
stadt = Raum()
stadt._init_("Stadt","stein",[],[],{},"Eine kleine Stadt.")

strasse = Raum()
strasse._init_("Strasse","stein",[],[],{},"Eine Strasse, die sich in weite Ferne erstreckt.")


bruecke = Raum()
bruecke._init_("Bruecke","stein",[],[],{},"Eine alte Steinbruecke.")

teich = Raum()
teich._init_("Teich","wasser",["Seerosen"],[],{},"Ein ruhiger Teich")

neueVerbindung(stadt,"s",strasse)
neueVerbindung(strasse,"s",bruecke)
neueVerbindung(bruecke,"n",strasse)
neueVerbindung(strasse,"n",stadt)
neueVerbindung(stadt,"o",teich)
neueVerbindung(teich,"w",stadt)


#Erstellen und platzieren von Objekten
schwert = Objekt()
schwert._init_("Schwert","Ein Eisenschwert")
objektPlatzieren(schwert,bruecke)

schluessel = Objekt()
schluessel._init_("Schluessel","Ein verrosteter Schluessel")
objektPlatzieren(schluessel,stadt)




shell(strasse)
