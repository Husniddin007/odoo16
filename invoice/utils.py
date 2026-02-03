# Birliklar va o'nliklar
birlar = ["", "bir", "ikki", "uch", "to'rt", "besh", "olti", "yetti", "sakkiz", "to'qqiz"]
onlar = ["", "o'n", "yigirma", "o'ttiz", "qirq", "ellik", "oltmish", "yetmish", "sakson", "to'qson"]
darajalar = ["", "ming", "million", "milliard"]

def number_to_words(num: int) -> str:
    if num == 0:
        return "nol"
    
    result = ""
    daraja = 0
    while num > 0:
        part = num % 1000
        if part != 0:
            yuz = part // 100
            on = (part // 10) % 10
            bir = part % 10

            qism = ""
            if yuz:
                qism += f"{birlar[yuz]} yuz "
            if on or bir:
                qism += f"{onlar[on]} {birlar[bir]} "
            if darajalar[daraja]:
                qism += f"{darajalar[daraja]} "
            result = qism + result
        num //= 1000
        daraja += 1
    return result.strip().capitalize()

def float_to_words(amount: float) -> str:
    som_str, tiyin_str = str(round(amount, 2)).split(".")
    som = int(som_str)
    tiyin = int(tiyin_str.ljust(2, "0"))

    som_text = number_to_words(som)
    tiyin_text = number_to_words(tiyin)

    return f"{som_text} so'm {tiyin_text} tiyin"






if __name__ == "__main__":
    amount = 56789123.792
    print(float_to_words(amount=amount))





