import csv

KIRISH_FAYL = "talabalar.csv"
CHIQISH_FAYL = "filtrlangan_talabalar.csv"

yonalish = input("Yo'nalish: ").strip()

talabalar = []

try:
    with open(KIRISH_FAYL, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        ustunlar = reader.fieldnames

        for qator in reader:
            try:
                qator["ball"] = int(qator["ball"])
            except (KeyError, ValueError):
                print(f"Ogohlantirish: noto'g'ri qator o'tkazib yuborildi: {qator}")
                continue

            if qator["yonalish"].strip().lower() == yonalish.lower():
                talabalar.append(qator)

except FileNotFoundError:
    print(f"Xatolik: {KIRISH_FAYL} fayli topilmadi.")
else:
    talabalar.sort(key=lambda t: t["ball"], reverse=True)

    with open(CHIQISH_FAYL, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ustunlar)
        writer.writeheader()
        writer.writerows(talabalar)

    print(f"{len(talabalar)} ta talaba topildi.")
    print(f"Natijalar {CHIQISH_FAYL} fayliga yozildi.")