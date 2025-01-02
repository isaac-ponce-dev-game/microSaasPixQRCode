from fastapi import APIRouter
from src.core.pix.application.service.generate_pix_qrcode import (
    CreatePixQrCodeService,
    InputCreatePixQrCode,
)
from src.fastapi.routers.dto.input import CreatePixQrcodeInput

router = APIRouter()


@router.post("/pix-qrcode")
def create(input: CreatePixQrcodeInput ):
    service = CreatePixQrCodeService()
    response = service.execute(InputCreatePixQrCode(value=input.value, key=input.key))

    return {"image_url": response.image_url}