voto = 15
temperatura = 22
if voto >= 18:
    print(f"Esame superato con {voto}! Vamos! 🚀")
else:
    print("Niente da fare, ci vediamo al prossimo appello. ☕")

for i in range(1, 3):
    print(f"Iterazione numero {i}")

if temperatura > 30:
    print("Fa caldo! 🌞")
else:
    if temperatura < 10:
        print(f"Fa freddo! 🥶 e con un voto di {voto}")
    else:
        print(f"Temperatura attuale: {temperatura}°C e non si sta male")

if temperatura == 22:
    print("Temperatura perfetta! 😎")
elif temperatura == 23:
    print("Temperatura ottima! 😎")
else:
    print("Temperatura non ideale! 🥵")
    