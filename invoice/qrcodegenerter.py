import qrcode
from PIL import Image


def genqrcode(url,box_size,border):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img_grayscale = qr.make_image(fill_color='black',black_color='white')
    img_rgb = img_grayscale.convert('RGB')
    return img_rgb


if __name__ == "__main__":
    url = "https://www.example.com"
    print(genqrcode(url=url))