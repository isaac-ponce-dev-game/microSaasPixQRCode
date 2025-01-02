from src.core.pix.application.service.dto.pix_qrcode import InputCreatePixQrCode, OutputCreatePixQrCode
from src.core.pix.model.entity import Pix


class CreatePixQrCodeService:
    def execute(self, request: InputCreatePixQrCode) -> OutputCreatePixQrCode:
        pix = Pix(value=request.value, key=request.key)
        payload = pix.generate_payload()
        image_name = f"{pix.key+pix.value}.png"
        pix.qr_code.generate_qr_code(payload,image_name)

        return OutputCreatePixQrCode(image_url=pix.qr_code.image_url)