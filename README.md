# ChatBot Tortas el Arbolito

## Introduccion
ChatBot desarrollado en python implementado en Telegram, que permite generar ordenes para el negocio de Tortas el Arbolito

## Comandos
Los comandos se dividen en dos partes, los que atienden al cliente y al negocio
### Cliente
_/start_
```
Hola! Soy el Bot de la casa del Arbolito.
Aqui podras encargar tu torta.
Contamos con un horario de atencion de 11:00 a 21:00
de Lunes a Viernes
Por donde empezar /help
```
_/help_
```
Podiras comenzar mirando nuestros menus, seguro te agrada algo /menu
```

_/menu_
```
Conoce nuestro menu!
/tortas
    .
    .
    .
/postres
```

_/tortas_
Cada comando listado anteriormnete genera un menu nuevo, estos comandos dependen de los prodcutos dados de alta.
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
__/ordenar_tortas__
Genera un teclado con las opciones encontradas
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

__/mi_pedido__
Muestra la orden generada de los productos agregados
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

__/confirmar_pedido__
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

__/cancelar_pedido__
```
Orden Cancelada
```

### Negocio
_/help_
```
Podiras comenzar mirando nuestros menus, seguro te agrada algo /menu
```

##

##