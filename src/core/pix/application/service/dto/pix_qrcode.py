from dataclasses import dataclass


@dataclass
class InputCreatePixQrCode:
    value: str
    key : str

@dataclass
class OutputCreatePixQrCode:
    image_url: str