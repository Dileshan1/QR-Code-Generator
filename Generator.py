import qrcode

qr=qrcode.QRCode(box_size=15,border=1)


def qr_gen(link):
    qr.add_data(link)
    qr.make()
    img = qr.make_image(fill_color="black", back_color="white", )

    return img
