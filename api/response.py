from modelResponse import Fulfillment

fulfillmentMessages = {"fulfillmentMessages": [
    {
        "card": {
            "title": "Fordez",
            "subtitle": "catalogo de productos para la venta",
            "imageUri": "https://i.imgur.com/tzWhjX3.png",
            "buttons": [
                {
                        "text": "Agregar al carrito",
                        "postback": "carrito"
                },
                {
                    "text": "Mas detalle",
                    "postback": "detalle"
                },
                {
                    "text": "Comprar",
                    "postback": "comprar"
                }
            ]
        }
    }

]}


def saludo(saludo: Fulfillment) -> dict:
    Saludo = saludo
    return Saludo


def response(dataOrigin, dataNlp,) -> dict:
    if (dataOrigin['source'] == "facebook"):
        response = saludo('hoa lucy tumaco')
    else:
        response = fulfillmentMessages
    return response
