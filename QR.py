import qrcode
from PIL import Image
im=qrcode.make('www.ncku.edu.tw')
im.show()
