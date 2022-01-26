# Karas Ausgangsposition wird dahinbgehend angepasst,
# dass sie neben einen Baum gestellt wird, damit die
# Befehle der while-Schleife unten ausgef�hrt werden k�nnen.
kara.move()
kara.putLeaf()
kara.turnRight()
kara.move()
kara.putLeaf()

# Der Z�hler dient als Abbruchbedingung f�r das gesamte
# Programm, da es sich umm ein Viereck handelt 4.
zaehler = 4

while zaehler != 0: # Hier wird der Z�hler genutzt.
    # Kara bewegt sich nach vorne und legt ggf. ein
    # Kleeblatt ab, wie rechts von ihr ein Baum ist.
    while kara.treeRight():
        kara.move()
        if not kara.onLeaf(): # Reine Vorsichtsma�nahme
            kara.putLeaf() # Ggf. wird ein Kleeblatt gesetzt
        
        # Am Ende muss sie sich nat�rlich noch in Richtung
        # der n�chsten Baumreihe drehen.
        if not kara.treeRight():
            kara.turnRight()

    # Nach dem Drehen ist es n�tig sie einen Schritt nach
    # vorne zu bringen, da sie sich sonst nicht rechts neben
    # sich einen Baum vorfindet und somit Baumreihe durch
    # die while-Schleife nicht umgangen werden kann.
    kara.move()
    if not kara.onLeaf(): # Reine Vorsichtsma�nahme
        kara.putLeaf() # Ggf. wird ein Kleeblatt gesetzt
    
    # Der Z�hler wird bei jeder Iteration um 1 verringert
    # um die while-Schleife zu beenden.
    zaehler = zaehler - 1

# Kara wird in die gew�nschte Endposition gebracht.
kara.move()
kara.putLeaf()

kara.move()
kara.turnRight()

kara.move()

# Kara wird umgedreht.
kara.turnRight()
kara.turnRight()