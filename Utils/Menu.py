import json
from telebot import types

msg_general="Contamos con:\n{}\nTe gustaria ordenar? /ordenar_{}\nVolver al menu /menu"
msg_comida_corrida="""\
Comida corrida por ${}
Nuestro guiso del dia: {}
Nuestros platillos:{}
Complementos:{}
\
"""

def get_file(file_menu):
    try:
        with open(file_menu, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print("File not Found: "+file_menu)
        return "Error"

def get_menu(file_menu):
    menu=get_file(file_menu)
    info="Conoce nuestro menu!"
    for key,value in menu["menu"].items():
        if key!="ingredientes":
            info+="\n/"+key
    return info

def get_info(file_menu,opc_menu):
    menu=get_file(file_menu)
    if opc_menu in menu["menu"]:
        info=""
        if opc_menu != "comida_corrida":
            for x in menu["menu"][opc_menu]:
                info += x["nombre"] + " $"+x["precio"]+"\n"
            if opc_menu=="tortas":
                info+="\n+$5.00 Por ingrediente Extra"
        else:
            info = get_comida_corrida(menu,opc_menu)
        return msg_general.format(info,opc_menu)
    return "Lo siento no cuento con esta informacion"

def get_comida_corrida(menu,opc_menu):
    platillos=""
    complementos=""
    for x in menu["menu"][opc_menu]["platillos"]:
        platillos+="\n\t\t"+x
    for x in menu["menu"][opc_menu]["complementos"]:
        complementos+="\n\t\t"+x
    return msg_comida_corrida.format(menu["menu"][opc_menu]["precio"],
                                    menu["menu"][opc_menu]["guiso_del_dia"],
                                    platillos,
                                    complementos)
                                    
def busca_producto(file_menu,producto):
    menu=get_file(file_menu)
    for key,value in menu["menu"].items():
        if key != "comida_corrida":
            for x in value:
                if x["nombre"]==producto:
                    return x["precio"]
    return "0"


def get_main_keyboard(file_menu,opc_menu):
    menu=get_file(file_menu)
    markup = types.ReplyKeyboardMarkup(row_width=3)
    for x in menu["menu"][opc_menu]:
        markup.add(types.KeyboardButton(x["nombre"]))
    markup.add(types.KeyboardButton('Quitar teclado'))
    return markup

def get_clear_keyboard():
    return types.ReplyKeyboardRemove(selective=False)