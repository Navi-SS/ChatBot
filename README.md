# ChatBot Tortas el Arbolito

## Introduccion
ChatBot desarrollado en python implementado en Telegram, que permite generar ordenes para el negocio de Tortas el Arbolito

## Comandos
Los comandos se dividen en dos partes, los que atienden al cliente y al negocio
### Cliente
__/start__:Muestra una breve introduccion
```
Hola! Soy el Bot de la casa del Arbolito.
Aqui podras encargar tu torta.
Contamos con un horario de atencion de 11:00 a 21:00
de Lunes a Viernes
Por donde empezar /help
```
__/help__:Te sugiere por donde comenzar
```
Podiras comenzar mirando nuestros menus, seguro te agrada algo /menu
```

__/menu__:Muestra el menu del negocio
```
Conoce nuestro menu!
/tortas
    .
    .
    .
/postres
```

__/tortas__:Cada comando listado anteriormnete genera un menu nuevo, estos comandos dependen de los prodcutos dados de alta.
```
Contamos con:
Torta Jamon $20.00
Torta Pierna $20.00
Torta Queso de Puerco $20.00
Torta Salchica $20.00
Torta Milanesa $30.00
Torta Hawaiana $33.00
Torta Cubana $50.00

+$5.00 Por ingrediente Extra
Te gustaria ordenar? /ordenar_tortas
Volver al menu /menu

```
__/ordenar_tortas__:Genera un teclado con las opciones encontradas
```
Torta Jamon
Torta Pierna
Torta Queso de Puerco
Torta Salchica
Torta Milanesa
Torta Hawaiana
Torta Cubana
Quitar Teclado
```

__/mi_pedido__:Muestra la orden generada de los productos agregados
```
Este es el pedido: 
Torta Pierna $20.00
Torta Jamon $20.00
Torta Queso de Puerco $20.00
Torta Jamon $20.00
Total: $80.0
Confirmar pedido: /confirmar_pedido
Cancelar pedido: /cancelar_pedido
Agregar mas cosas: /menu
```

__/confirmar_pedido__:Genera el pedido y se le notifica al usuario
```
Clinete:
Ya hice el pedido

Negocio:
Pedido: 
Torta Pierna $20.00
Torta Jamon $20.00
Torta Queso de Puerco $20.00
Torta Jamon $20.00
Total: $80.0
```

__/cancelar_pedido__:Cancela el pedido
```
Orden Cancelada
```

### Negocio
__/pedidos__:Lista los pedidos generados
```
Estos son los pedidos activos

Pedido #1009
Torta Pierna $20.00
Torta Jamon $20.00
Torta Queso de Puerco $20.00
Torta Jamon $20.00
Total: $80.0
/finalizar_orden_1009

Pedido #1010
Torta Pierna $20.00
Torta Queso de Puerco $20.00
Torta Salchica $20.00
Total: $60.0
/finalizar_orden_1010
```
__/finalizar_orden_*__
```
Negocio:
Notificando al usuario

Usuario:
Tu orden esta lista.

```