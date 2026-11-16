import csv

FAYL = "savdo.csv"
tushum = {}

try:
    with open(FAYL, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for qator in reader:
            try:
                kategoriya = qator["kategoriya"].strip()
                narx = float(qator["narx"])
                miqdor = int(qator["miqdor"])
            except (KeyError, ValueError):
                print(f"Ogohlantirish: noto'g'ri qator o'tkazib yuborildi: {qator}")
                continue

            tushum[kategoriya] = tushum.get(kategoriya, 0) + narx * miqdor

except FileNotFoundError:
    print(f"Xatolik: {FAYL} fayli topilmadi.")
else:
    if tushum:
        for kategoriya, summa in sorted(tushum.items(), key=lambda x: x[1], reverse=True):
            matn = f"{summa:,.0f}".replace(",", " ")
            print(f"{kategoriya}: {matn} so'm")

        eng_yaxshi = max(tushum, key=tushum.get)
        print(f"Eng daromadli kategoriya: {eng_yaxshi}")
    else:
        print("Hisoblash uchun ma'lumot topilmadi.")