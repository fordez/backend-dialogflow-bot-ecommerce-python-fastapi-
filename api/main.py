from requestModel import RequestOriginal, RequestNlp
from response import response
from fastapi import FastAPI, Body

api = FastAPI()


@api.post("/webhook")
async def webhook(
        queryResult: RequestNlp = Body(..., embed=True),
        originalDetectIntentRequest: RequestOriginal = Body(..., embed=True),
        session: str = Body(..., embed=True)):

    intent = queryResult.intent.displayName
    menssage = queryResult.queryText
    languageCode = queryResult.languageCode
    parameters = dict(queryResult.parameters)
    platform = originalDetectIntentRequest.source

    return response()
