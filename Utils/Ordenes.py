import json
from telebot import types

def get_file(file_ordenes):
    try:
        with open(file_ordenes, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print("File not Found: "+file_ordenes)
        return "Error"

def get_orden(file_ordenes,chat_id,mensaje):
    orden="Lo siento no tengo alguna orden registrada"
    data=get_file(file_ordenes)
    for x in data:
        if x["chat_id"] == chat_id and x["status"]==500:
            orden=mensaje
            total=0
            for y in x["orden"]:
                orden+="\n"+y["nombre"]+" $"+y["precio"]
                total+=float(y["precio"])
            orden+="\nTotal: $"+str(total)
    return orden

def update_orden(file_ordenes,chat_id,no_orden,status,status_search):
    orden=0
    data=get_file(file_ordenes)
    for x in data:
        if (x["id"]==no_orden or x["chat_id"] == chat_id )and x["status"]==status_search:
            x["status"]=status
            orden=x["chat_id"]
            with open(file_ordenes,"w") as outfile:
                json.dump(data,outfile)
    return orden

def del_orden(file_ordenes,chat_id):
    orden="Lo siento no lo logramos cancelar"
    data=get_file(file_ordenes)
    for x in data:
        if x["chat_id"] == chat_id and x["status"]==500:
            data.remove(x)
            orden="Orden Cancelada"
            with open(file_ordenes,"w") as outfile:
                json.dump(data,outfile)
    return orden

def create_orden(file_ordenes,chat_id,name,producto):
    data=get_file(file_ordenes)
    if busca_orden(data,chat_id,producto) ==0:
        data.append({
            "id":1000+len(data),
            "chat_id":chat_id,
            "nombre":name,
            "status":500,
            "orden":[producto]
        })
    with open(file_ordenes,"w") as outfile:
        json.dump(data,outfile)

def busca_orden(data,chat_id,producto):
    for x in data:
        if x["chat_id"] == chat_id and x["status"]==500:
            x["orden"].append(producto)
            return x["chat_id"]
    return 0

def get_pedidos(file_ordenes):
    data=get_file(file_ordenes)
    orden=""
    for x in data:
        if x["status"]==400:
            orden+="\nPedido #"+str(x["id"])
            total=0
            for y in x["orden"]:
                orden+="\n"+y["nombre"]+" $"+y["precio"]
                total+=float(y["precio"])
            orden+="\nTotal: $"+str(total)+"\n /finalizar_orden_"+str(x["id"])+"\n"
    return orden

def pedido_nuevo():
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(types.KeyboardButton("Aceptar"))
    markup.add(types.KeyboardButton("Rechazar"))
    markup.add(types.KeyboardButton('Quitar teclado'))
    return markup