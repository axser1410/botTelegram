#import PIL.Image  #no se uso la libreria pil
import pyscreenshot
#import pyautogui #tampoco la pyautogui pero ambas podrian incorporar funciones interesantes
import telebot
import os
import glob

ruta = r"C:\Users\Alex\Desktop\fotos\prueba"
imagenes = "*.PNG"
lista_envio= glob.glob(ruta + os.sep + imagenes)
numero = len(lista_envio) #calcula la cantidad de elementos de esta variable(directorio)

nombreCarpeta = "botTelegram"
    

token = ""
bot = telebot.TeleBot(token)
#contadorMensajes = 1
def handle_messages(messages):
    for message in messages:
        chatid = message.chat.id
        chatname = message.chat.username
        chatidipropio = 00
        if message.content_type == "text":
            text = message.text
            if text == "/hola" or text == "/start":
                bot.send_message(chatid, "hola "+str(chatname)+"dime.  Los mensajes funcionales son: /hola /info /help /fotos /screen /exit \nPara interactuar con el bot se recomienda consultar en /info")
            if text == "/info":
                bot.send_message(chatid, "soy el bot programado de Al: quieres un saludo? Dime /hola!. Este bot fue creado exactamente el 22 de Noviembre a las 11:24. \n/hola y /start  mandan un saludo y muestra los comandos funcionales \n/info muestra la informacion de todos los comandos \n/help mestra los comandos disponibles \n/fotos muestra las imagenes de una determinada carpeta determinada por el administrador de este bot \n/screen toma captura a la pantalla del administrador y manda lo manda al ususario que interactua con el bot ")
            if text == "/help":
                bot.send_message(chatid, "hola "+str(chatname)+" dime.  Los mensajes funcionales son: /hola /info /help /fotos /screen /exit")
            if text == "/screen":
                im = pyscreenshot.grab()
                im.save('captura1.png')
                photo = open("C:/Users/Alex/Desktop/Telegram/"+nombreCarpeta+"/captura1.png", "rb")
                bot.send_photo(chatidipropio, photo) #para que mande la foto al usuario se debe cambiar chatidpropio por chatid
            if text == "apagar":
                    os.system("shutdown /s /t 1")
            if text == "/e x i t":
                bot.stop_polling()
            if text == "/fotos":
                for i in range(numero-1):
                    photo = open(lista_envio[i], "rb")
                    bot.send_photo(chatid, photo)
                    
                




bot.set_update_listener(handle_messages)
bot.infinity_polling()
