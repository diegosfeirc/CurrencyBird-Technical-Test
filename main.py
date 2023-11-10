from fastapi import FastAPI
from pydantic import BaseModel, Field
import requests

app = FastAPI()

class Payment(BaseModel):
    transfer_code: str = Field(alias="transferCode")
    amount: int 


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/payments")
def create_payment(payment: Payment):
    token = get_token()
    header = {"Authorization": token}
    request = requests.post("https://dev.developers-test.currencybird.cl/payment?email=dsfeir@uc.cl&transferCode=dsfeir@uc.cl", json=payment.model_dump(by_alias=True), headers=header)
    return request.json()
    

@app.get("/token")
def get_token():
    token = requests.get("https://dev.developers-test.currencybird.cl/token?email=dsfeir@uc.cl")
    return token.text

