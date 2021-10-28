from modelRequest import RequestOriginal, RequestNlp
from response import response
from fastapi import FastAPI, Body

api = FastAPI()


@api.post("/webhook")
async def webhook(
        queryResult: RequestNlp = Body(..., embed=True),
        originalDetectIntentRequest: RequestOriginal = Body(..., embed=True)):

    dataNlp = dict(queryResult)
    dataOrigin = dict(originalDetectIntentRequest)
    print(dataNlp)

    return response(dataOrigin, dataNlp)
