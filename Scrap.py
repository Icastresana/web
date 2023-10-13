import requests
from bs4 import BeautifulSoup

# URL de la página web
url = "https://hackmd.io/@w8tAmGnzT-qbgHkemaly6A/SEGUNDA-PARTE"

# Realiza una solicitud GET para obtener el contenido HTML de la página
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encuentra todos los elementos <a> que contienen enlaces acestream
    acestream_links = [a['href'] for a in soup.find_all('a') if a['href'].startswith('acestream://')]
    
    # Imprime los enlaces Acestream
    for link in acestream_links:
        print(link)
else:
    print("No se pudo acceder a la página web.")

