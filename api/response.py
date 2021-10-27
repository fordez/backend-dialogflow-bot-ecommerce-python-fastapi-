def response() -> dict:
    return {"fulfillmentMessages": [
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
            },
            "platform": "FACEBOOK"
        }

    ]}
