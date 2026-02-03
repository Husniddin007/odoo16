from PIL import Image,ImageDraw,ImageFont

from datetime import datetime

from qrcodegenerter import genqrcode
from utils import float_to_words


class Invoys:
    def __init__(self,img_width,img_hight,inv_number,
                 bank_name,account_number,bank_code,treasury_account,
                 STIR,payer_name,payment_type,amount,url,file_name):
        self.img_width = img_width
        self.img_hight = img_hight
        # self.inv_name = inv_name
        self.inv_number = inv_number
        self.bank_name = bank_name
        self.bank_code = bank_code
        self.account_number = account_number
        self.treasury_account = treasury_account
        self.STIR = STIR
        self.payer_name = payer_name
        self.payment_type = payment_type
        self.amount = amount
        self.url = url
        self.file_name = file_name
    
    def create_img(self):
        img = Image.new(mode="RGB",size=(self.img_width,self.img_hight),color='white')
        draw = ImageDraw.Draw(im=img)
        return img, draw
    
    def load_font(self, font_dir: str = "/usr/share/fonts/truetype/msttcorefonts/", 
                  name="Arial",size=20,bold=False):
        try:
            font_path= f"{font_dir}{name}{'_Black.ttf' if bold else '.ttf'}"
            font = ImageFont.truetype(font_path, size)
            print("✅ Shriftlar muvaffaqiyatli yuklandi.")
            return font
        except IOError:
            print(f"Xato: {font_path} fayli topilmadi. Standart shrift ishlatildi.")
            return ImageFont.load_default()
    
    def create_inv(self, margin = 36):
        # vertikal
        self.create_img().line(xy=(margin, margin - 15, margin, self.img_hight//2 - 36), fill='gray', width=1)
        self.create_img().line(xy=(15 * margin, self.img_hight//2 - 252, 15 * margin, self.img_hight//2 - 108), fill='gray', width=1)
        self.create_img().line(xy=(19 * margin, self.img_hight//2 - 252, 19 * margin, self.img_hight//2 - 72), fill='gray', width=1)
        # gorizantal
        self.create_img().line(xy=(margin, 2*margin, self.img_width - margin, 2*margin), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - margin, 3 * margin, 9 * margin, 3 * margin), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - 12 * margin, 4 * margin, 9 * margin, 4 * margin), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - margin, 4 * margin, self.img_width - 9 * margin, 4 * margin), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - margin, 5 * margin, 9 * margin, 5 * margin), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width -  margin, 6 * margin + 20, margin, 6 * margin + 20), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - 5*margin, 7 * margin + 20, margin, 7 * margin + 20), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - 5*margin, 10 * margin + 20, margin, 10 * margin + 20), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width - 5*margin, 11 * margin + 20, margin, 11 * margin + 20), fill='gray',width=1) 
        self.create_img().line(xy=(self.img_width, 12 * margin + 20, margin, 12 * margin + 20), fill='gray',width=1) 

        self.create_img().text(xy=(margin + 20, margin), text='ICHKI ISHLAR VAZIRLIGI', fill='black', font=self.load_font(bold=True))
        self.create_img().text(xy=(self.img_width - 12 * margin, margin), text=f'INVOYS N_{self.inv_number}', fill='black', font=self.load_font(bold=True))

        self.create_img().text(xy=(margin + 20, 2 * margin + 10), text="Bank nomi", fill='black', font=self.load_font())
        self.create_img().text(xy=(9 * margin + 10, 2 * margin + 10), text=self.bank_name, fill='black', font=self.load_font())

        self.create_img().text(xy=(margin + 20, 3 * margin + 10), text="Oluvchning hisob raqami", fill='black', font=self.load_font())
        self.create_img().text(xy=(9 * margin + 10, 3 * margin + 10), text=self.account_number, fill='black', font=self.load_font())
        # # sublinename
        self.create_img().text(xy=(self.img_width - 12 * margin, 3 * margin + 10), text="Bank kodi", fill='black', font=self.load_font())
        self.create_img().text(xy=(self.img_width - 8 * margin, 3 * margin + 10), text=self.bank_code, fill='black', font=self.load_font())

        self.create_img().text(xy=(margin + 20, 4 * margin + 10), text="G'azna hisobvarag'i", fill='black', font=self.load_font())
        self.create_img().text(xy=(9 * margin + 10, 4 * margin + 10), text=self.treasury_account, fill='black', font=self.load_font())
        # # sublinename
        self.create_img().text(xy=(self.img_width - 12 * margin, 4 * margin + 10), text="STIR", fill='black', font=self.load_font())
        self.create_img().text(xy=(self.img_width - 8 * margin, 4 * margin + 10), text=self.STIR, fill='black', font=self.load_font())

        self.create_img().text(xy=(margin + 20, 5 * margin + 15), text="To'lovchi", fill='black', font=self.load_font())
        self.create_img().text(xy=(9 * margin + 10, 5 * margin + 15), text=self.payer_name, fill='black', font=self.load_font(bold=True))

        self.create_img().text(xy=(2 * margin, 6 * margin + 25), text="To'lov turi", fill='black', font=self.load_font())
        self.create_img().text(xy=(1.5 * margin, 6.5 * margin + 25), text=self.payment_type, fill='black', font=self.load_font())

        self.create_img().text(xy=(16 * margin, 6 * margin + 25), text="Sana",fill="black", font=self.load_font())
        self.create_img().text(xy=(15.5 * margin, 8 * margin + 25), text=datetime.now().strftime('%d.%m.%Y'),fill="black", font=self.load_font())

        self.create_img().text(xy=(20 * margin, 6 * margin + 25), text="Pul miqdori", fill='black', font=self.load_font())
        self.create_img().text(xy=(20 * margin, 8 * margin + 25), text=f"{self.amount:.2f} so'm", fill='black', font=self.load_font())

        self.create_img().text(xy=(2 * margin, 10 * margin + 25), text="To'lovchi", fill='black', font=self.load_font())
        self.create_img().text(xy=(16 * margin, 10 * margin + 25), text="Jami",fill="black", font=self.load_font())
        self.create_img().text(xy=(20 * margin, 10 * margin + 25), text=f"{self.amount:.2f} so'm", fill='black', font=self.load_font())

        # self.create_img().''.text(xy=(20 * margin, 11 * margin + 25), text=f"{amount} so'm {(amount%10):.2f} tiyin" , fill='black', font=self.load_font())
        self.create_img().text(xy=(2 * margin, 11 * margin + 25), text=float_to_words(amount=self.amount) , fill='black', font=self.load_font())

        self.create_img().text(xy=(28.5 * margin, 11 * margin + 25), text='00000125287', fill='black', font=self.load_font())

        qr_code = genqrcode(url=self.url,box_size=5,border=3)
        self.create_img().paste(qr_code, (28 * margin, 7* margin))
        self.create_img().paste(self.self.create_img(), (0, self.img_hight - 14 * margin))
        self.create_img().save(self.file_name)
        print(f"✅ Invoice saved as {self.file_name}")
        

if __name__ == "__main__":
    obj = Invoys(
        img_width = 1178,
        img_hight = 976,
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
        url = "https://www.example.com",
        file_name = 'test.png'
    )
