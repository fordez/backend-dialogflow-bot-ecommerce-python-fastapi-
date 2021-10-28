class Fulfillment:
    text: str

    def __init__(self, text):
        self.text = text

    def tex(self) -> dict:
        return {"fulfillmentText": self.text}


class Card:
    title: str
    subtitle: str
    imageUri: str
    buttonText1: str
    postback1: str
    buttonText2: str
    postback2: str
    buttonText3: str
    postback3: str

    def __init__(self, title, subtitle, imageUri,
                 buttonText1, postback1,
                 buttonText2, postback2,
                 buttonText3, postback3):

        self.title = title
        self.subtitle = subtitle
        self.imageUri = imageUri
        self.buttonText1 = buttonText1
        self.postback1 = postback1
        self.buttonText2 = buttonText2
        self.postback2 = postback2
        self.buttonText3 = buttonText3
        self.postback3 = postback3

    def resposeCard(self) -> dict:
        return {"fulfillmentMessages": [
            {
                "card": {
                    "title": self.title,
                    "subtitle": self.subtitle,
                    "imageUri": self.imageUri,
                    "buttons": [
                        {
                            "text": self.buttonText1,
                            "postback": self.postback1
                        },
                        {
                            "text": self.buttonText2,
                            "postback": self.postback2
                        },
                        {
                            "text": self.buttonText3,
                            "postback": self.postback3
                        }
                    ]
                }
            }
        ]}
