import qrcode
import qrcode.constants
from PIL import Image
qr=qrcode. QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,border=4)
qr.add_data("htps://www.facebook.com/tisa.akter.501")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("fb_profile.png")
