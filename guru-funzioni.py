# 1. Qui DEFINIAMO la funzione (la fabbrica). 
# Accetta un parametro in ingresso che chiamiamo "voto_esame"
def controlla_voto(voto_esame):
    if voto_esame >= 18:
        return f"Esame superato con {voto_esame}! 🚀"
    else:
        return f"Voto {voto_esame}: Ci vediamo al prossimo appello. ☕"

# 2. Qui la USIAMO (la chiamiamo in causa) quante volte vogliamo!
esame_algebra = controlla_voto(28)
esame_analisi = controlla_voto(15)
esame_python = controlla_voto(30)

# Stampiamo i risultati
print(esame_algebra)
print(esame_analisi)
print(esame_python)

collezione_stanze = ["PS5", "PS4", "PS3", "PS2", "PS1", "Nintendo Switch", "Xbox Series X", "Xbox One", "PC Gaming"]

def playstation(modello):
    if modello == "PS5":
        return "La PS5 è la console più potente di Sony! 🎮"
    elif modello == "PS4":
        return "La PS4 è una console ottima e popolare! 🎮"
    elif modello == "PS3":
        return "La PS3 è una console storica di Sony! 🎮"
    elif modello == "PS2":
        return "La PS2 è una console leggendaria di Sony! 🎮"
    elif modello == "PS1":
        return "La PS1 è la console che ha rivoluzionato il mondo dei videogiochi! 🎮"
    else:
        return f"{modello} non è una console PlayStation valida."
    
for console in collezione_stanze:
    risultato = playstation(console)
    print(risultato)