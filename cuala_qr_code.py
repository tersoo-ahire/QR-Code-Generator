# Import QR Code modules and packages 
import pyqrcode, png
from pyqrcode import QRCode


# String which represents the QR Code
link = "https://cutt.ly/DLhl4Rv"


# Generate QR Code
qr_code = pyqrcode.create(link)


# Create and save the png file naming it as "cuala_qr.png"
qr_code.png("cuala_qr.png", scale = 8)


# Create and save the svg file naming it as "cuala_qr.svg"
qr_code.svg("cuala_qr.svg", scale = 8)
