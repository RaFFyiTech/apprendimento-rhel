temperature_settimana = [9, 23, 35, 24, 8, 19, 37]

for t in temperature_settimana:
    if t > 30:
        print(f"Temperatura {t}°C: Fa caldo! 🌞")
    elif t < 10:
        print(f"Temperatura {t}°C: Fa freddo! 🥶")
    else:
        print(f"Temperatura {t}°C: Temperatura attuale: {t}°C e non si sta male")
    