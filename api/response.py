from typing import Text
from modelResponse import Fulfillment, Card


def fulfillment(text) -> dict:
    fulfillmenText = Fulfillment(text)
    return fulfillmenText.tex()


def card(title, subtitle, imageUri,
         buttonText1, postback1,
         buttonText2, postback2,
         buttonText3, postback3) -> dict:

    card = Card(title, subtitle, imageUri,
                buttonText1, postback1,
                buttonText2, postback2,
                buttonText3, postback3)

    return card.resposeCard()


def response(dataOrigin, dataNlp,) -> dict:
    if (dataOrigin['source'] != "facebook"):
        response = fulfillment("Hola madre")
    else:
        title = "Fordez"
        subtitle = "catalogo de productos para la venta"
        imageUri = "https://i.imgur.com/tzWhjX3.png"
        buttonText1 = "Agregar al carrito"
        postback1 = "carrito"
        buttonText2 = "Mas detalle"
        postback2 = "detalle"
        buttonText3 = "Comprar"
        postback3 = "comprar"

        response = card(title, subtitle, imageUri,
                        buttonText1, postback1,
                        buttonText2, postback2,
                        buttonText3, postback3)
    return response
