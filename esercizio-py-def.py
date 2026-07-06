pesi_ordini = [1, 5, 2, 12, 0.5, 7]

def assegna_veicolo(kg):
    if kg > 10:
        return "Troppo pesante! Consegna con Furgone 🚚"
    elif kg <= 2:
        return "Leggero! Consegna con Drone 🚁"
    else:
        return "Peso medio! Consegna con Bicicletta 🚲"

for peso in pesi_ordini:
    risultato = assegna_veicolo(peso)
    print(f"Ordine di {peso} kg: {risultato}")