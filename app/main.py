import qrcode

data = "My message here" # sample string data to save in image
img = qrcode.make(data)

qrcode_filename = "qrcode.jpg" 
img.save(qrcode_filename)