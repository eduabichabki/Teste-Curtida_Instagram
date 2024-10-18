import pyautogui
import webbrowser
from time import sleep
import pyperclip

site = "https://www.instagram.com/"

#Abrir site do Instagram
webbrowser.open_new_tab(site)
sleep(2)

#Abrir a pagina de se conectar no instagram
pyautogui.moveTo(1490,227, duration=1)
pyautogui.scroll(-1000)
pyautogui.moveTo(1584,611, duration=1)
pyautogui.leftClick()
sleep(2)

def escrever_dados(dado):
    pyperclip.copy(dado)
    pyautogui.hotkey("ctrl", "v")

#Escrever dados do login
escrever_dados("eduabichabki")
sleep(1)
pyautogui.press("tab")
sleep(1)
escrever_dados("@Edudados94")
sleep(1)
pyautogui.press("enter")
sleep(6)

#Salvar informacoes de login
pyautogui.moveTo(1528,721, duration=1)
pyautogui.leftClick()
sleep(2)

#Pesquisar pagina
pyautogui.moveTo(1590,187, duration=1)
pyautogui.leftClick()
sleep(1)
escrever_dados("wealth")
pyautogui.moveTo(1549,279, duration=2.5)
pyautogui.leftClick()
sleep(2)

#Selecionar a ultima postagem
pyautogui.moveTo(1276,652, duration=1)
pyautogui.leftClick()
sleep(1)
pyautogui.moveTo(1277,739, duration=1)
pyautogui.leftClick()
sleep(2)

#Curtir a postagem
imagem = pyautogui.locateCenterOnScreen("S_Curtida.png")
if imagem == None:
    sleep(86400)
else:
    pyautogui.moveTo(x=imagem[0], y=imagem[1], duration=1)
    pyautogui.leftClick()
    pyautogui.moveTo(1413,837, duration=1)
    pyautogui.leftClick()
    sleep(1)
    pyautogui.moveTo(1510,942, duration=1)
    pyautogui.leftClick()
    sleep(1)
    escrever_dados("TOP!")
    sleep(1)
    pyautogui.moveTo(1695,946, duration=1)
    pyautogui.leftClick()
    sleep(86400)