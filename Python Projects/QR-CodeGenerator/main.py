import qrcode as qr

link = input("Enter your link : ")

rename = input("Rename your file : ")

img = qr.make(link)
img.save(rename + ".png")
