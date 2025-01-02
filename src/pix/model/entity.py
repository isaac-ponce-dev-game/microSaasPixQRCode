from dataclasses import dataclass, field
import crcmod
import qrcode

from src.pix.model.object_value import (ADDITIONAL_DATA_FIELD_TEMPLATE,
                                        COUNTRY_CODE,
                                        CRC_PLACEHOLDER,
                                        MERCHANT_CATEGORY_CODE,
                                        PAYLOAD_FORMAT_INDICATOR, 
                                        POINT_OF_INITIATION_METHOD,
                                        TRANSACTION_CURRENCY,
)
from src.qrcode.model.entity import QRCode

from typing import Callable

def default_qrcode() -> QRCode:
    return QRCode(image_url="default_image_url")  # Substitua por um valor válido para sua aplicação.

@dataclass
class Pix:
    value: str
    key: str
    payload: str = ""
    nome_receiver: str = "N"
    city_receiver: str = "C"
    qr_code: QRCode = field(default_factory=default_qrcode)  # Use a função auxiliar aqui.

    def generate_payload(self) -> str:
        merchant_account_information = f"0014BR.GOV.BCB.PIX01{len(self.key):02d}{self.key}"
        merchant_account_information_length = f"{len(merchant_account_information):02d}"
        
        transaction_amount = f"54{len(self.value):02d}{self.value}"
        merchant_name = f"59{len(self.nome_receiver):02d}{self.nome_receiver}"
        merchant_city = f"60{len(self.city_receiver):02d}{self.city_receiver}"


        # Montagem do payload
        payload_code = (
            PAYLOAD_FORMAT_INDICATOR
            + POINT_OF_INITIATION_METHOD
            + f"26{merchant_account_information_length}{merchant_account_information}"
            + MERCHANT_CATEGORY_CODE
            + TRANSACTION_CURRENCY
            + transaction_amount
            + COUNTRY_CODE
            + merchant_name
            + merchant_city
            + ADDITIONAL_DATA_FIELD_TEMPLATE
            + CRC_PLACEHOLDER
        )

        # Validar payload gerado antes do cálculo do CRC
        print("Payload Code (pre CRC):", payload_code)
     
        # Cálculo do CRC
        payload = payload_code + self.calculate_crc16(payload_code)

        print("Final Payload:", payload)  # Verificar o payload final gerado
        return payload

    def calculate_crc16(self, payload: str) -> str:
        crc16_func = crcmod.mkCrcFun(0x11021, initCrc=0xFFFF, rev=False, xorOut=0x0000)
        crc = hex(crc16_func(payload.encode('utf-8'))).upper()[2:]
        return crc.zfill(4)
