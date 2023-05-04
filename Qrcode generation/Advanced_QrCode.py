from asyncio import QueueEmpty
from turtle import fillcolor
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=15, border= 3)
qr.add_data("https://pypi.org/project/qrcode/")
qr.make(fit=True)
img = qr.make_image(fillcolor= "black", back_color= "white")
img.save("Qrcode_document_site.png")