#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from Utils.Menu import get_info,get_menu,get_main_keyboard,get_clear_keyboard,busca_producto
from Utils.Ordenes import get_orden,create_orden,del_orden,update_orden,pedido_nuevo,get_pedidos
API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)
file_menu="Recursos/Info.json"
file_ordenes="Recursos/Ordenes.json"

with open('bienvenida.txt','r') as f:
    msg_bienvenida = f.read()

@bot.message_handler(commands=['start'])
def start_chat(message):
    bot.send_message(message.chat.id,msg_bienvenida)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    menu="Podiras comenzar mirando nuestros menus, seguro te agrada algo /menu"
    bot.send_message(message.chat.id,menu)

@bot.message_handler(commands=['menu'])
def send_welcome(message):
    menu=get_menu(file_menu)
    bot.send_message(message.chat.id,menu)

@bot.message_handler(commands=['mi_pedido'])
def send_welcome(message):
    orden=get_orden(file_ordenes,message.chat.id,"Este es el pedido: ")
    if orden!="Lo siento no tengo alguna orden registrada":
        orden+="\n Confirmar pedido: /confirmar_pedido"
        orden+="\n Cancelar pedido: /cancelar_pedido"
        orden+="\n Agregar mas cosas: /menu"
    bot.send_message(message.chat.id,orden)

@bot.message_handler(commands=['confirmar_pedido'])
def send_welcome(message):
    orden=get_orden(file_ordenes,message.chat.id,"Pedido: ")
    chat_id=update_orden(file_ordenes,message.chat.id,0,400,500)
    if chat_id!=0:
        menu="Ya hice el pedido"
    else:
        menu="Lo siento no logre realizar el pedido"
    bot.send_message(message.chat.id,menu)
    bot.send_message(1520943427,orden)

@bot.message_handler(commands=['cancelar_pedido'])
def send_welcome(message):
    menu=del_orden(file_ordenes,message.chat.id)
    bot.send_message(message.chat.id,menu)

@bot.message_handler(commands=['pedidos'])
def send_welcome(message):
    mensaje="Lo siento no tengo informacion acerca de esto"
    if message.chat.id == 1520943427:
        mensaje=get_pedidos(file_ordenes)
        if mensaje!="":
            mensaje="Estos son los pedidos activos\n"+mensaje
        else:
            mensaje="No tenemos pedidos el dia de hoy"
    bot.send_message(message.chat.id,mensaje)    

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    producto=busca_producto(file_menu ,message.text)
    if "/ordenar" in message.text:
        markup = get_main_keyboard(file_menu,message.text.replace("/ordenar_",""))
        bot.send_message(message.chat.id, "Generando orden: ", reply_markup=markup)
    elif "/pedido" in message.text:
        print("peido")
    elif "/finalizar_orden" in message.text:
        id_orden=message.text.replace("/finalizar_orden_","")
        chat_id=update_orden(file_ordenes,0,int(id_orden),100,400)
        if chat_id!=0:
            bot.send_message(1520943427,"Notificando al usuario")
            bot.send_message(chat_id,"Tu orden esta lista.")
        else:
            bot.send_message(1520943427,"No encontre una orden relacionada")
    elif "/" in message.text:
        menu=get_info(file_menu,message.text.replace("/",""))
        bot.send_message(message.chat.id, menu)
    elif producto!="0":
        add={"nombre":message.text,"precio":producto}
        create_orden(file_ordenes,message.chat.id,message.chat.first_name,add)
        string = "Se agrego {} al pedido. \nDesas  ordenar algo mas del menu? /menu\nRealizar pedido /mi_pedido".format(message.text)
        bot.send_message(message.chat.id,string)
    elif message.text == "Quitar teclado":
        markup = get_clear_keyboard()
        bot.send_message(message.chat.id,"Ver menus /menu", reply_markup=markup)
    else:
        bot.send_message(message.chat.id,"No te entiendo aun, podrias usar /help para comnezar")

bot.polling(True)