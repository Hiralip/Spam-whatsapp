#Importa libreria
import pyautogui as pg, webbrowser as web, time as tm
#Ingresar a la web (Recuerda cambiar el phone)
web.open('https://web.whatsapp.com/send?phone=+56990737896')
#Esperar 20 segundos para ingresar a la pagina
tm.sleep(20)
#Ciclo para mandar mensaje (puedes cambiar el rango y el mensaje)
for i in range(20):
    pg.write('Hola, soy un bot')
    pg.press('enter')
