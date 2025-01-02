from dataclasses import dataclass

import qrcode.constants
from qrcode.main import QRCode as QRCODE

@dataclass
class QRCode:
    image_url: str

    def generate_qr_code(self, payload: str, image_url: str)-> str:
        qr = QRCODE(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4)
        qr.add_data(payload)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",back_color="white")
        img.save(image_url)
        self.image_url = image_url
        return image_url