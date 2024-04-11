import pyautogui as GUI
import time

#Tempo entre os comandos GUI
GUI.PAUSE = 0.5

#Primeiro passo abrir a tecla windowns para pesquisar o navegador
GUI.press("win")
#Pesquisar o navegador
GUI.write("Opera gx")
#Confirmar para entrar no navegador
GUI.press("enter")
#Pesquisar a url que queremos 
GUI.write("https://web.whatsapp.com")
#Apertar enter para entrar no site da url
GUI.press("enter")
#Tempo para esperar a página carregar
time.sleep(5)
#Clicar no campo de pesquisa do whatsapp
GUI.click(x=240, y=152)
#Pesquisar o nome de quem queremos
GUI.write("Yasmim")
#Pressionar enter para entrar no contato
GUI.press("enter")


#Escrever a mensagem repetidas vezes
for i in range(10000):
    GUI.write("Eu fui dormir é deixei enviando mensagem,bom dia quando acordar")
    GUI.press("enter")
