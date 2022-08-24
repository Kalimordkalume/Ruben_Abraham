import requests
from bs4 import BeautifulSoup as BS
#Objetivos: Necesitamos localizar la URL, y cargar su información en nuestro script.
URL="https://www.wakfu.com/es/mmorpg"
datos_web=requests.get(URL)
#print(datos_web)

respuesta=requests.get("https://www.wakfu.com/es/mmorpg")

if respuesta:
    print('Success!')
else:
    print("An error has occurred.")
print(respuesta)
