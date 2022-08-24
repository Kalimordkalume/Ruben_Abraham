import random
opciones=["piedra","papel","tijeras"]
tirada_humano=opciones[2]
tirada_pc=random.choice(opciones)
print("has elegido: "+tirada_humano + " pc ha elegido: "+tirada_pc)