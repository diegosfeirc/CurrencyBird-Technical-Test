from sqlalchemy.orm import Session

import models, schemas

def get_payment_by_transfer_code(db: Session, transfer_code: str):
    return db.query(models.Payment).filter(models.Payment.transfer_code == transfer_code).first()

def create_payment(db: Session, payment: schemas.PaymentCreate):
    db_payment = models.Payment(transfer_code=payment.transfer_code, amount=payment.amount)
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment