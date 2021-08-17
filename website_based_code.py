pip install qrcode

import qrcode

# enter your URL link within the .make method
img = qrcode.make("https://www.youtube.com/")

# name the QR code within the .save method
final_image = img.save("youtubeQR.jpg")
