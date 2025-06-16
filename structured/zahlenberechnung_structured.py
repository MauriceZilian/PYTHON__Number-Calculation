# Initialisierung
summe = 0.0
anzahl = 0
minimum = None
maximum = None

# Eingabeschleife
while True:
    eingabe = input("Bitte eine Zahl eingeben (oder 'fertig' zum Beenden): ")

    if eingabe.lower() == 'fertig':
        break

    try:
        zahl = float(eingabe)
        summe += zahl
        anzahl += 1

        if minimum is None or zahl < minimum:
            minimum = zahl

        if maximum is None or zahl > maximum:
            maximum = zahl

    except ValueError:
        print("Ungültige Eingabe. Bitte eine gültige Zahl eingeben.")
        
# Ausgabe
print("\nErgebnisse:")
print("Anzahl:", anzahl)
print("Summe:", summe)

if anzahl > 0:
    durchschnitt = summe / anzahl
    print("Durchschnitt:", durchschnitt)
else:
    print("Kein Durchschnitt berechenbar.")

print("Minimum:", minimum)
print("Maximum:", maximum)

