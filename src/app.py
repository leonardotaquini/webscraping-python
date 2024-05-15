import requests
import re
from bs4 import BeautifulSoup
import json


# URL de la página
url_base = "https://listado.mercadolibre.com.ar/_Container_hot-sale-celulares#DEAL_ID=MLA30697&S=landingHubhot-sale&V=15&T=Special-withoutLabel&L=CELULARES&deal_print_id=82567a90-12b9-11ef-8c3b-3fc8f0b72e9c&c_id=special-withoutlabel&c_element_order=2&c_campaign=CELULARES&c_uid=82567a90-12b9-11ef-8c3b-3fc8f0b72e9c"
result = {}
try:    
    # Hacer la solicitud HTTP a la página
    response = requests.get(url_base)
 
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')
    # Obtengo todos los links de la página
    links = soup.find_all('a')
    # Recorro los links y muestro la URL
    for link in links:
        url = link['href']
        exp = re.compile(r'^https://www.mercadolibre.com.ar/')
        if exp.match(url):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            h1 = soup.find_all('h1')
            p = soup.find_all('p')
            print(str(p).encode('utf-8'))
            print(p)
            if h1 and p:
                result[url] = [str(h1), str(p)]
                print(result[url])
            else:
                result[url] = []     

    # result = json.dumps(result)
except Exception as e:
    print(f"Error al acceder a la página: {e}")



