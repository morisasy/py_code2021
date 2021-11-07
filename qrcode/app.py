# pip install qrcode
import pyqrcode
import png
from pyqrcode import QRCode 

s = 'Python.hub'

url = pyqrcode.create(s)

url.svg('myqr.svg', scale = 8)
url.png('myqr.svg', scale = 6)
