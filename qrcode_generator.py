import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

value=input('enter any url link:')
qr.add_data(value)
qr.make(fit=True)

img = qr.make_image(fill_color=(4,17,67), back_color=(237,232,245))
img.save("YourQrcode.png")