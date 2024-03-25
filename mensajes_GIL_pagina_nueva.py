# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:35:44 2023

@author: miguel
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

from fake_useragent import UserAgent

import datetime
import locale
from babel.dates import format_date, Locale
import time
import emoji
from io import StringIO
import sys
import telegram
import re

import os
import psutil
from urllib.parse import quote


def enviar_mensaje_estadisticas(mensaje):
    mensaje_codificado = quote(mensaje)
    url_MCP = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID_MIGUEL}&text={mensaje_codificado}"
    url_GIL = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID_GIL}&text={mensaje_codificado}"
    (requests.get(url_MCP).json());
    (requests.get(url_GIL).json());
    #bot.send_message(chat_id=CHAT_ID_MIGUEL, text=mensaje)
    #bot.send_message(chat_id=CHAT_ID_GIL, text=mensaje)

TOKEN = "6198330283:AAE1ervpNxlWDJ02z7o-1YOtZ1p7TjOS9Eo"
# ID del chat donde se enviarán los mensajes

CHAT_ID_MIGUEL = 461058179
CHAT_ID_GIL=205183332

# Crear un objeto bot
bot = telegram.Bot(token=TOKEN)

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39"


# Lista de palabras clave que corresponden a países de habla hispana y latinoamericana
paises_hispanohablantes = ["españa", "argentina", "bolivia", "chile", "colombia", "costa_rica", "cuba", "ecuador", "el_salvador", "guatemala", "honduras", "méxico", "nicaragua", "panamá", "paraguay", "perú", "puerto_rico", "república_dominicana", "uruguay", "venezuela"]
spanish_speaking_countries = ["Spain", "Argentina", "Bolivia", "Chile", "Colombia", "Costa_Rica", "Cuba", "Ecuador", "El_Salvador", "Guatemala", "Honduras", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto_Rico", "Dominican_Republic", "Uruguay", "Venezuela"]
continentes_spain=["europa","américa","oceanía","asia","áfrica"]
continentes_spain=["Europe","America","Oceania","Asia","Africa"]

continente_emoji = {
        "américa ": "🌎 ",
        "europa ": "🌍 ",
        "asia ": "🌏 ",
        "áfrica ": "🌍 ",
        "oceanía ": "🌏 "
    }
continente_emoji_ing = {
        "America ": "🌎 ",
        "Europe ": "🌍 ",
        "Asia ": "🌏 ",
        "Africa ": "🌍 ",
        "Oceania ": "🌏 "
    }
# URL de la página web a analizar
url = 'https://futboljobs.com/bolsa-empleo-futbol/'


edge_options=Options()
ua=UserAgent()
userAgent=ua.edge
edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
edge_options.add_experimental_option('useAutomationExtension', False)
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_options.add_argument('--no-sandbox')
edge_options.add_argument('--disable-extensions')

#edge_options.add_argument('--window-size=1920,1080')
#edge_options.add_argument('--headless')
#edge_options.add_argument('--disable-gpu')
edge_options.add_argument('--allow-running-insecure-content')
#edge_options.add_argument("--headless")
edge_options.add_argument(f'user-agent={user_agent}')

# Realizar una solicitud GET a la URL y obtener el contenido HTML
driver = webdriver.Edge(options=edge_options)
driver.get('https://futboljobs.com/bolsa-empleo-futbol/')

# boton=driver.find_element(By.CLASS_NAME,'asp_showmore')
# boton.click()
time.sleep(5)
html = driver.page_source
driver.quit()

        
# Crear un objeto BeautifulSoup a partir del contenido HTML
soup = BeautifulSoup(html, 'html.parser')

# Encontrar todas las ofertas de trabajo en la página
# ofertas_de_trabajo = soup.find_all('div', {'class': "resdrg"})

ofertas1=soup.find_all('div', {'class': "fjo-main-column fjo-job-link fjo-flex"})

driver = webdriver.Edge(options=edge_options)
driver.get('https://futboljobs.com/bolsa-empleo-futbol/page/2/')

# boton=driver.find_element(By.CLASS_NAME,'asp_showmore')
# boton.click()
time.sleep(5)
html = driver.page_source
driver.quit()


PROCNAME = "msedge.exe" # or chromedriver or IEDriverServer
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()
        
soup = BeautifulSoup(html, 'html.parser')

ofertas2=soup.find_all('div', {'class': "fjo-main-column fjo-job-link fjo-flex"})
ofertas=ofertas1 + ofertas2

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

fecha_hoy = datetime.date.today()
#fecha_hoy=fecha_hoy-datetime.timedelta(days=1) #en caso de querer el dia anterior y que ente en la lista

fecha_actual=format_date(fecha_hoy,"dd MMM yy", locale='es')
fecha_actual_2=format_date(fecha_hoy,"dd MMM yyyy", locale='es')
# Convertir el texto a fecha
#print('OFERTAS '+fecha_actual_2.upper())


# Redirige la salida estándar al objeto StringIO
output = StringIO()
sys.stdout = output

print( '*OFERTAS '+fecha_actual_2.upper() + '*\n' )
for oferta in ofertas:
    titulo = oferta.find('h2', {'class': 'fjo-rolename'}).text.strip()
    link = oferta.find('h2', {'class': 'fjo-rolename'}).a['href']
    fecha = oferta.find(class_='fjo-top-meta').text.strip()
   # ubicacion = oferta.find('div', {'class': 'asp_res_text'}).text.strip()
    #ubicacion = ubicacion.split('|')[-1].strip()
    # if(titulo.startswith('🏆')):
    #     titulo= titulo[1:].strip()
    # txt_aux=re.sub(r"[^\w\sÀ-ÖØ-öø-ÿ]", '',ubicacion.lower())
    #ubicacion = txt_aux.replace(' ', '_')    
    # if(ubicacion[-1]=='_'):
    #     ubicacion=ubicacion[0:-1]
    # ubicacion = ubicacion.replace('eeuu', 'estados_unidos')
    # ubicacion = ubicacion.replace('corea', 'corea_del_sur')
    # bandera=':bandera_'+ubicacion.lower()+': '
    # if(txt_aux in continente_emoji):
    #     bandera=f"{continente_emoji[txt_aux] }"
             
    if(fecha.lower().find("hoy")):
        # if(ubicacion.lower() in continente_emoji):
        #     print( bandera + titulo) 
        # else:
            print(titulo)
            print('👉 ', link +'\n')
        # Verificar si la ubicación corresponde a un país de habla hispana o latinoamericana
        # if (ubicacion.lower() in paises_hispanohablantes):
        #     print('👉 ', link+ ' (Español)' '\n')
        # else:
        #     print('👉 ', link+ ' (Inglés)' '\n')

        


# Redirige la salida estándar de vuelta a su valor predeterminado
sys.stdout = sys.__stdout__

# Obtiene todo lo que se ha impreso
mensaje_spain = output.getvalue()

# Imprime la salida guardada
# with open('archivo_espanol.txt', mode='a', encoding='utf-8') as archivo:
#     archivo.write(mensaje_spain)

enviar_mensaje_estadisticas(mensaje_spain)


4
# Imprime la salida guardada
# with open('archivo_ingles.txt', mode='a', encoding='utf-8') as archivo:
#     archivo.write(mensaje_ingles)
    
 