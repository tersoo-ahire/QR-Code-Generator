# Import QR Code modules and packages 
import pyqrcode, png
from pyqrcode import QRCode


# String which represents the QR Code
link = "https://www.binance.com/"


# Generate QR Code
qr_code = pyqrcode.create(link)


# Create and save the png file naming it as "binanceqr.png"
qr_code.png("binanceqr.png", scale = 8)


# Create and save the svg file naming it as "binance_qr.svg"
qr_code.svg("binanceqr.svg", scale = 8)
