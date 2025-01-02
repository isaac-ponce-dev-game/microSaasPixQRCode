from fastapi import FastAPI
from src.fastapi.routers.create_pix_qrcode import router as create_pix_qrcode_router

app = FastAPI()

app.include_router(create_pix_qrcode_router)