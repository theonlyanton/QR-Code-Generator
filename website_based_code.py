pip install qrcode

import qrcode

# enter your URL link within the .make method
img = qrcode.make("https://www.youtube.com/")

# create and save your QR code inside a variable
# name the QR code within the .save method
final_image = img.save("youtubeQR.jpg")
