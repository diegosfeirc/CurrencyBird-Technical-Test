from pydantic import BaseModel, Field

class PaymentBase(BaseModel):
    transfer_code: str = Field(alias="transferCode")
    amount: int

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True