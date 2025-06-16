# Initialisierung von Variablen
summe = 0.0
anzahl = 0
minimum = None
maximum = None

# Schleife zur Eingabe von Zahlen
while True:
        
        line = input("Bitte eine Zahl eingeben (oder 'fertig' zum beenden): ")

        #Abbruchbedingung
        if line == 'fertig':
            break
            
        try:
            # Umwandlung der Eingabe in eine Zahl
            zahl = float(line)
            
            # Aktualisierung von Summe und Anzahl
            summe = summe + zahl
            anzahl = anzahl + 1
            
            # Bestimmung von Minimum und Maximum
            if minimum is None or zahl < minimum:
                minimum = zahl
                
            if maximum is None or zahl > maximum:
                maximum = zahl
            
        # Fehlerbehandlung bei ungültiger Eingabe
        except ValueError:
            print('Ungültige Eingabe. Bitte eine gültige Zahl eingeben.')

# Ausgabe der Ergebnisse
print('Anzahl:' , anzahl)
print('Summe:' , summe)

durchschnitt = summe / anzahl
print('Durchschnitt:' , durchschnitt)

print('Minimum:' , minimum)
print('Maximum:' , maximum)

