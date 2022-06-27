#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Usuario
#
# Created:     13/06/2022
# Copyright:   (c) Usuario 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Bot telegram

from config import *
import telebot # para manejar la api de telegram
import requests
from telebot.types import ReplyKeyboardMarkup # para crear botones
from telebot.types import ForceReply # Para citar un mensage
from telebot.types import ReplyKeyboardRemove # par eliminar botones

# Instanciamos el bot
bot = telebot.TeleBot(TOKEN)

# variable global en la que guardaremos los datos del usuario
usuarios = {}


# Start

@bot.message_handler(commands = ["start", "ayuda", "help"])

def start(message):
    """ Da la bienvenida al usuario del bot """
    botones = ReplyKeyboardRemove()
    saludo  = 'Hola, soy el chatbot de la catedra de <b> Programacion </b> ' + '\U0001F44B' +'\n'
    texto1  = "¿ que puedo hacer por vos hoy ? "
    foto    = open("./imagenes/bot5.png", "rb")
    bot.send_message(message.chat.id, saludo, parse_mode ="html",reply_markup=botones)
    bot.send_photo(message.chat.id, foto, "")
    bot.send_message(message.chat.id, texto1, parse_mode ="html",reply_markup=botones)
    msg = bot.send_message(message.chat.id, "Usa el comando /info para informacion", reply_markup=botones)
    bot.register_next_step_handler(msg, info)



@bot.message_handler(commands=["info"])
def info(message):
    """ Menu con las opciones que brinda el bot al usuario"""
    cid   = message.chat.id
    texto = message.text
    usuarios[cid] = texto
    botones = ReplyKeyboardMarkup(one_time_keyboard=True,
    input_field_placeholder="Pulsa un boton",
    resize_keyboard=True)
    botones.add("Inicio", "Inscripcion", "Aula Virtual", "Cursada", "Pandemia",
    "Horarios", "Aulas", "Herramientas", "Docentes", "Asistencia")
    msg = bot.send_message(message.chat.id, "¿ Cual es tu duda ?", reply_markup = botones)
    #msg = bot.send_message(message.chat.id, "¿ Cual es tu duda ?", reply_markup=markup)
    bot.register_next_step_handler(msg, comprobar_mensaje)


"""
    if message.text == "Inicio" or message.text == "Inscripcion" or message.text == " Aula Virtual" or message.text == "Cursada" or message.text == "Pandemia" or message.text == "Horarios" or message.text == " Aulas" or message.text == "Herramientas" or message.text == "Docentes" or message.text == "Asistencia":
        cadena == message.text
    msg = bot.send_message(message.chat.id, cadena)
"""

    #bot.register_next_step_handler(msg, inscripcion)

def comprobar_mensaje(message):
    """ Comprueba que opcion ejecuta """
    botones = ReplyKeyboardRemove()
    cid = message.chat.id

    print("... " + message.text)
    msg = bot.send_message(message.chat.id, "-", reply_markup = botones)
    #bot.register_next_step_handler(msg, inicio)

    if message.text == "Inicio":
        mensaje = 'La clases inician el dia 17 de agosto de 2022'
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Inscripcion":
        mensaje  = 'Recuerda que para cursar debes tener aprobada o regularizada <b> Elementos de Programacion </b>' +'\n'
        mensaje += 'Debes completar el formulario que te enviamos por mail \n'
        mensaje += '<b>Formulario</b>: https://forms.gle/3pkn9WmyNzfCyJN48  \n'
        mensaje += '<i>Importante En el formulario te preguntaremos el esquema de vacunacion Sea cual sea tu respuesta, nada impide que curses la materia</i>'
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Aula Virtual":
        mensaje  = 'La catedra te matricularà en el aula virtual (AV) \n'
        mensaje += 'Para matricularte usamos el correo electronico que proporcionaste en el formulario de inscripcion \n'
        mensaje += '<i><b>El aula virtual se encuentra instalada en</b></i> : '
        mensaje += 'https://exavirtual.unsa.edu.ar/enrol/index.php?id=533 \n'
        mensaje += 'Una vez que llenes el formulario podras acceder al AV desde el dia 17/08/2022 \n'
        mensaje += 'Importante: Si llenas el formulario despues del 17/08/2022 para acceder al AV debes esperar 24 hs habiles de haber llenado el formulario'
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Cursada":
        mensaje = 'La modalidad de cursado de Programacion es bimodal;presencial y virtual. Las clases y las consultas se ofreceran, algunas virtuales y otras presenciales.'
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Pandemia":
        mensaje = 'Por cuestiones de aforo,el/la alumno/a debe asistir solamente a las clases asignadas.'
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Horarios":
        mensaje  = "<b>El horario de cada comision se informara oportunamente</b>"+'\n'
        mensaje += '\n'
        mensaje += 'Programacion tiene una carga semanal de 10 horas; 4 horas de teoria y 6 de practica. Se cursa los dias lunes, miercoles y viernes.\n\n'
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Aulas":
        mensaje = "<i><b>Las aulas y laboratorios para el cursado de la materia se informara oportunamente en la puerta del box de la Lic. Marcela Lopez (BOX 19)</b></i>"
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Docentes":
         mensaje   = '<b>Teoria</b> :\n\n'
         mensaje  += '\u2705 Lic. Marcela Lopez BOX 19\n'
         mensaje  += '\u2705 Lic. Ariel Rivera  BOX 27\n\n'
         mensaje   += '<b>Practica</b>:\n\n'
         mensaje += '\u2705 Lic. Carina Jimena Reyes LAB 3\n'
         mensaje +='\u2705 C.U. Eduardo Fernandez   LAB 3\n'
         mensaje +='\u2705 Lic. Cecilia Espinoza    LAB 3\n'
         mensaje +='\u2705 Lic. Claudio Vargas      LAB 3\n'
         mensaje +='\u2705 Lic. Claudia Ibarra      LAB 3\n'
         msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
         bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Herramientas":

         unidad1 = open("./pdfs/unidad1.pdf","rb")
         unidad2 = open("./pdfs/unidad2.pdf","rb")
         unidad3 = open("./pdfs/unidad3.pdf","rb")
         unidad4 = open("./pdfs/unidad4.pdf","rb")
         unidad5 = open("./pdfs/unidad5.pdf","rb")
         unidad6 = open("./pdfs/unidad6.pdf","rb")
         unidad7 = open("./pdfs/unidad7.pdf","rb")

         bot.send_document(message.chat.id, unidad1, caption= "Unidad Teorica 1")
         bot.send_document(message.chat.id, unidad2, caption= "Unidad Teorica 2")
         bot.send_document(message.chat.id, unidad3, caption= "Unidad Teorica 3")
         bot.send_document(message.chat.id, unidad4, caption= "Unidad Teorica 4")
         bot.send_document(message.chat.id, unidad5, caption= "Unidad Teorica 5")
         bot.send_document(message.chat.id, unidad6, caption= "Unidad Teorica 6")
         bot.send_document(message.chat.id, unidad7, caption= "Unidad Teorica 7")

         practica1 = open("./pdfs/tp1.pdf","rb")
         practica2 = open("./pdfs/tp2.pdf","rb")
         practica3 = open("./pdfs/tp3.pdf","rb")
         practica4 = open("./pdfs/tp4.pdf","rb")
         practica5 = open("./pdfs/tp5.pdf","rb")
         practica6 = open("./pdfs/tp6.pdf","rb")
         practica7 = open("./pdfs/tp7.pdf","rb")
         practica8 = open("./pdfs/tp8.pdf","rb")
         practica9 = open("./pdfs/tp9.pdf","rb")
         practica10 = open("./pdfs/tp10.pdf","rb")

         bot.send_document(message.chat.id, practica1, caption= "tp1")
         bot.send_document(message.chat.id, practica2, caption= "tp2")
         bot.send_document(message.chat.id, practica3, caption= "tp3")
         bot.send_document(message.chat.id, practica4, caption= "tp4")
         bot.send_document(message.chat.id, practica5, caption= "tp5")
         bot.send_document(message.chat.id, practica6, caption= "tp6")
         bot.send_document(message.chat.id, practica7, caption= "tp7")
         bot.send_document(message.chat.id, practica8, caption= "tp8")
         bot.send_document(message.chat.id, practica9, caption= "tp9")
         bot.send_document(message.chat.id, practica10, caption= "tp10")
         mensaje = " La catedra utiliza el <b> Software Zinjai :</b>" +'\n'
         mensaje += 'http://zinjai.sourceforge.net/'


         msg = bot.send_message(message.chat.id, mensaje, reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
         bot.send_message(message.chat.id, "/info \n")

    elif message.text == "Asistencia":
        mensaje = "<b> Asistencia </b>: '\n'" + "https://script.google.com/a/~/macros/s/AKfycbwgJDE7IGRHsgaUgvKMIZn0USS8QiORr9qfjDzmXDBH8dCwKUXHFo3GRKOp7GgH4Eg/exec"
        msg = bot.send_message(message.chat.id, mensaje,reply_markup = botones, parse_mode = "html", disable_web_page_preview= True)
        bot.send_message(message.chat.id, "/info \n")


"""
def enviarMensaje(mensaje):
    requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
              data={'chat_id': idGrupo, 'text': mensaje, 'parse_mode': 'HTML'})

"""

def enviarMensaje(mensaje):
    requests.post('https://api.telegram.org/bot' + TOKEN + '/sendMessage',
    data={'chat_id' : -1001421122637, 'text': mensaje, 'parse_mode' : 'html'}
    )

"""
def enviarDocumento(ruta):
    requests.post('https://api.telegram.org/bot' + idBot + '/sendDocument',
              files={'document': (ruta, open(ruta, 'rb'))},
              data={'chat_id': idGrupo, 'caption': 'imagen caption'})

"""


































if __name__ == '__main__':
    mensaje = "Te envio la asistencia del dia de la fecha : " + '\n'
    mensaje = "Asistencia : " + "https://script.google.com/a/~/macros/s/AKfycbwgJDE7IGRHsgaUgvKMIZn0USS8QiORr9qfjDzmXDBH8dCwKUXHFo3GRKOp7GgH4Eg/exec"
    enviarMensaje("Hola, soy un bot y estoy mandando un mensaje a Telegram usando Python")
    enviarMensaje(mensaje)
    # configuramos los comandos disponibles en el bot
    bot.set_my_commands([
    telebot.types.BotCommand("/start", "da la bienvenida"),
    telebot.types.BotCommand("/info", "muestra la informacion que brinda el bot")
    ])
    print("Iniciando el bot")
    bot.infinity_polling()
