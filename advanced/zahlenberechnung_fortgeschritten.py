# Initialisierung einer leeren Liste um die Zahlen zu speichern
Liste = []

# Begrüßung und Anleitung
print("Willkommen! Dieses Programm hilft Ihnen dabei, das Maximum, Minimum und den Durchschnitt Ihrer Eingaben zu berechnen.")
print("Geben Sie eine Zahl ein und drücken Sie Enter. Geben Sie 'fertig' ein, um das Programm zu beenden.")

while True:
    eingabe = input('\nGeben Sie eine Zahl ein: ')
    
    if eingabe.lower() == 'fertig':
        break
        
    try:
        zahl = float(eingabe)
        Liste.append(zahl)
        
    except ValueError:
        print('Ungültige Eingabe! Bitte geben Sie eine gültige Zahl ein.')

# Überprüfen, ob gültige Zahlen eingegeben wurden
if Liste:
    
    # Berechnungen
    Durchschnitt = sum(Liste) / len(Liste)
    
    # Ausgabe
    print("\n" + "="*40)      # Eine Trennlinie für eine bessere visuelle Struktur
    print(f"Ergebnisse:")
    print(f"---------------------------")
    print(f"Maximum: {max(Liste):.2f}")      # Formatierung auf 2 Dezimalstellen
    print(f"Minimum: {min(Liste):.2f}")
    print(f"Durchschnitt: {Durchschnitt:.2f}")
    print(f"---------------------------")
    print("="*40)
else:
    print("\nEs wurden keine gültigen Zahlen eingegeben.")
