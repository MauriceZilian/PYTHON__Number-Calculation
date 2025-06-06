# Initialisierung von Variablen
summe = 0.0
anzahl = 0
minimum = None
maximum = None

# Schleife zur Eingabe von Zahlen
while True:
        
        line = input("Bitte eine Zahl eingeben (oder 'done' zum beenden): ")

        #Abbruchbedingung
        if line == 'done':
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

# Durchschnitt nur berechnen, wenn mindestents eine Zahl eingegeben wurde
if anzahl > 0:
    durchschnitt = summe / anzahl
    print('Durchschnitt:' , durchschnitt)
else:
    print('Kein Durchschnitt berechenbar.')

print('Minimum:' , minimum)
print('Maximum:' , maximum)

