from pydantic import BaseModel


class CreatePixQrcodeInput(BaseModel):
    value: str
    key: str