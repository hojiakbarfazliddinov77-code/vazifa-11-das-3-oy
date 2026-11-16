jami = 0
eng_kop_ism = None
eng_kop_soat = 0

try:
    with open("ish_vaqti.txt", "r", encoding="utf-8") as fayl:
        for qator in fayl:
            qator = qator.strip()
            if not qator:
                continue

            qismlar = qator.split()
            ism = qismlar[0]

            try:
                soat = int(qismlar[1])
                if soat < 0:
                    raise ValueError
            except (IndexError, ValueError):
                print(f"Ogohlantirish: {ism} uchun soat qiymati noto'g'ri.")
                continue

            jami += soat
            if soat > eng_kop_soat:
                eng_kop_soat = soat
                eng_kop_ism = ism

except FileNotFoundError:
    print("Xatolik: ish_vaqti.txt fayli topilmadi.")
else:
    print(f"Jami ish soati: {jami}")
    if eng_kop_ism:
        print(f"Eng ko'p ishlagan: {eng_kop_ism} — {eng_kop_soat} soat")