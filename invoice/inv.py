from PIL import Image, ImageDraw,ImageFont

from datetime import datetime

from qrcodegenerter import genqrcode
from utils import float_to_words


def invoice_generator(inv_number,bank_name,account_number,bank_code, 
treasury_account, STIR, payer_name, payment_type, amount,url, file_name='inv.png',):
    img_width = 1178
    img_hight = 976

    img = Image.new(mode='RGB',size=(img_width, img_hight), color='white')
    draw = ImageDraw.Draw(im=img)

    FONT_DIR = "/usr/share/fonts/truetype/msttcorefonts/"
    try:
        font_title = ImageFont.truetype(f"{FONT_DIR}Arial_Black", 24)
        font_text = ImageFont.truetype(f"{FONT_DIR}Arial.ttf",20)
        font_emoji = ImageFont.truetype(f"{FONT_DIR}DejaVuSans.ttf",35)
        print("✅ Shriftlar muvaffaqiyatli yuklandi.")
    except IOError:
        print(f"Xato: {FONT_DIR} fayli topilmadi. Standart shrift ishlatildi.")
        font_title = None
        font_text = None


    margin = 36
    # vertikal
    draw.line(xy=(margin, margin - 15, margin, img_hight//2 - 36), fill='gray', width=1)
    draw.line(xy=(15 * margin, img_hight//2 - 252, 15 * margin, img_hight//2 - 108), fill='gray', width=1)
    draw.line(xy=(19 * margin, img_hight//2 - 252, 19 * margin, img_hight//2 - 72), fill='gray', width=1)

    # gorizantal
    draw.line(xy=(margin, margin - 15 , img_width - margin, margin - 15), fill='gray',width=1) 
    draw.line(xy=(margin, 2*margin, img_width - margin, 2*margin), fill='gray',width=1) 
    draw.line(xy=(img_width - margin, 3 * margin, 9 * margin, 3 * margin), fill='gray',width=1) 
    draw.line(xy=(img_width - 12 * margin, 4 * margin, 9 * margin, 4 * margin), fill='gray',width=1) 
    draw.line(xy=(img_width - margin, 4 * margin, img_width - 9 * margin, 4 * margin), fill='gray',width=1) 
    draw.line(xy=(img_width - margin, 5 * margin, 9 * margin, 5 * margin), fill='gray',width=1) 
    draw.line(xy=(img_width -  margin, 6 * margin + 20, margin, 6 * margin + 20), fill='gray',width=1) 
    draw.line(xy=(img_width - 5*margin, 7 * margin + 20, margin, 7 * margin + 20), fill='gray',width=1) 
    draw.line(xy=(img_width - 5*margin, 10 * margin + 20, margin, 10 * margin + 20), fill='gray',width=1) 
    draw.line(xy=(img_width - 5*margin, 11 * margin + 20, margin, 11 * margin + 20), fill='gray',width=1) 
    draw.line(xy=(img_width, 12 * margin + 20, margin, 12 * margin + 20), fill='gray',width=1) 
    x1, img_width = 15, img_width
    dash, gap = 15, 10
    x = x1
    while x < img_width:
        draw.line((x, 13 * margin + 20, x + dash, 13 * margin + 20), fill="gray", width=2)
        x += dash + gap


    draw.text(xy=(margin + 20, margin), text='ICHKI ISHLAR VAZIRLIGI', fill='black', font=font_title)
    draw.text(xy=(img_width - 12 * margin, margin), text=f'INVOYS N_{inv_number}', fill='black', font=font_title)

    draw.text(xy=(margin + 20, 2 * margin + 10), text="Bank nomi", fill='black', font=font_text)
    draw.text(xy=(9 * margin + 10, 2 * margin + 10), text=bank_name, fill='black', font=font_text)

    draw.text(xy=(margin + 20, 3 * margin + 10), text="Oluvchning hisob raqami", fill='black', font=font_text)
    draw.text(xy=(9 * margin + 10, 3 * margin + 10), text=account_number, fill='black', font=font_text)
    # # sublinename
    draw.text(xy=(img_width - 12 * margin, 3 * margin + 10), text="Bank kodi", fill='black', font=font_text)
    draw.text(xy=(img_width - 8 * margin, 3 * margin + 10), text=bank_code, fill='black', font=font_text)

    draw.text(xy=(margin + 20, 4 * margin + 10), text="G'azna hisobvarag'i", fill='black', font=font_text)
    draw.text(xy=(9 * margin + 10, 4 * margin + 10), text=treasury_account, fill='black', font=font_text)
    # # sublinename
    draw.text(xy=(img_width - 12 * margin, 4 * margin + 10), text="STIR", fill='black', font=font_text)
    draw.text(xy=(img_width - 8 * margin, 4 * margin + 10), text=STIR, fill='black', font=font_text)

    draw.text(xy=(margin + 20, 5 * margin + 15), text="To'lovchi", fill='black', font=font_text)
    draw.text(xy=(9 * margin + 10, 5 * margin + 15), text=payer_name, fill='black', font=font_title)

    draw.text(xy=(2 * margin, 6 * margin + 25), text="To'lov turi", fill='black', font=font_text)
    draw.text(xy=(1.5 * margin, 6.5 * margin + 25), text=payment_type, fill='black', font=font_text)

    draw.text(xy=(16 * margin, 6 * margin + 25), text="Sana",fill="black", font=font_text)
    draw.text(xy=(15.5 * margin, 8 * margin + 25), text=datetime.now().strftime('%d.%m.%Y'),fill="black", font=font_text)

    draw.text(xy=(20 * margin, 6 * margin + 25), text="Pul miqdori", fill='black', font=font_text)
    draw.text(xy=(20 * margin, 8 * margin + 25), text=f"{amount:.2f} so'm", fill='black', font=font_text)

    draw.text(xy=(2 * margin, 10 * margin + 25), text="To'lovchi", fill='black', font=font_text)
    draw.text(xy=(16 * margin, 10 * margin + 25), text="Jami",fill="black", font=font_text)
    draw.text(xy=(20 * margin, 10 * margin + 25), text=f"{amount:.2f} so'm", fill='black', font=font_text)

    # draw.text(xy=(20 * margin, 11 * margin + 25), text=f"{amount} so'm {(amount%10):.2f} tiyin" , fill='black', font=font_text)
    draw.text(xy=(2 * margin, 11 * margin + 25), text=float_to_words(amount=amount) , fill='black', font=font_text)

    draw.text(xy=(28.5 * margin, 11 * margin + 25), text='00000125287', fill='black', font=font_text)

    draw.text(xy = (margin, 13 * margin), text = "✂️", fill="black", font=font_emoji)

    qr_code = genqrcode(url=url,box_size=5,border=3)
    img.paste(qr_code, (28 * margin, 7* margin))
    img.paste(img, (0, 0))
    img.paste(img, (0, img_hight - 13 * margin))




    img.save(file_name)
    print(f"✅ Invoice saved as {file_name}")

if __name__ == "__main__":
    invoice_generator(
        inv_number="56998512752299",
        bank_name="Moliya Vazirligi Yagona G'azna Xisobvarag'i",
        account_number='4011408606262873422105179',
        bank_code='00014',
        treasury_account='23402000300100001010',
        STIR='201122919',
        payer_name="Husniddin",
        payment_type="""
        916 - Chet el fuqoralariga va fuqoroligi bo'lmagan
        shaxslarga kirish yoki kirish-chiqish vizalarini
        berganlik hamda ularning amal qilishi muddatini
        uzaytirish boji (o'ttiz kungacha)""",
        amount = 56789123.792,
        url = "https://www.example.com"
    )
