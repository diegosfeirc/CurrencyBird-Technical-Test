from fastapi import FastAPI, Depends
import requests
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/payments")
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = crud.get_payment_by_transfer_code(db, transfer_code=payment.transfer_code)
    if db_payment:
        return "Payment already registered"
    else:
        db_payment = crud.create_payment(db=db, payment=payment)
        token = get_token()
        if token == "ERROR getting token, please try again later":
            return token
        else:
            header = {"Authorization": token}
            request = requests.post("https://prod.developers-test.currencybird.cl/payment?email=dsfeir@uc.cl&transferCode=dsfeir@uc.cl", json=payment.model_dump(by_alias=True), headers=header)
            if request.status_code == 200:
                return request.json()
            else:
                return "ERROR creating payment, please try again later"
    

@app.get("/token")
def get_token():
    token = requests.get("https://prod.developers-test.currencybird.cl/token?email=dsfeir@uc.cl")
    if token.status_code == 200:
        return token.text
    else:
        return "ERROR getting token, please try again later"

