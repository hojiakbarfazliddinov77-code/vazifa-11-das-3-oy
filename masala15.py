import csv
import os

import matplotlib.pyplot as plt

FAYL = "kitoblar.csv"
USTUNLAR = ["nom", "kategoriya", "muallif", "oqilgan"]


def kitoblarni_yuklash():
    """CSV fayldan kitoblar ro'yxatini o'qiydi."""
    kitoblar = []
    if not os.path.exists(FAYL):
        return kitoblar
    with open(FAYL, "r", encoding="utf-8", newline="") as f:
        for qator in csv.DictReader(f):
            try:
                kitoblar.append({
                    "nom": qator["nom"].strip(),
                    "kategoriya": qator["kategoriya"].strip(),
                    "muallif": qator["muallif"].strip(),
                    "oqilgan": int(qator["oqilgan"]),
                })
            except (KeyError, ValueError, TypeError):
                print(f"Ogohlantirish: noto'g'ri qator o'tkazib yuborildi: {qator}")
    return kitoblar


def kitoblarni_saqlash(kitoblar):
    """Kitoblar ro'yxatini CSV faylga yozadi."""
    with open(FAYL, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=USTUNLAR)
        writer.writeheader()
        writer.writerows(kitoblar)


def kitob_chiqarish(kitob):
    print(f"{kitob['nom']} | {kitob['kategoriya']} | "
          f"{kitob['muallif']} | {kitob['oqilgan']} marta")


def kitoblarni_korish(kitoblar):
    if not kitoblar:
        print("Kitoblar yo'q.")
        return
    for kitob in kitoblar:
        kitob_chiqarish(kitob)


def kitob_qoshish(kitoblar):
    nom = input("Kitob nomi: ").strip()
    kategoriya = input("Kategoriya: ").strip()
    muallif = input("Muallif: ").strip()
    try:
        oqilgan = int(input("Necha marta o'qilgan: "))
        if oqilgan < 0:
            raise ValueError
    except ValueError:
        print("Xatolik: o'qilgan soni butun va manfiy bo'lmagan son bo'lishi kerak.")
        return
    if not nom or not kategoriya or not muallif:
        print("Xatolik: barcha maydonlarni to'ldiring.")
        return

    kitoblar.append({"nom": nom, "kategoriya": kategoriya,
                     "muallif": muallif, "oqilgan": oqilgan})
    kitoblarni_saqlash(kitoblar)   # CSV fayl yangilanadi
    print("Kitob qo'shildi va fayl yangilandi.")


def kitob_qidirish(kitoblar):
    so_rov = input("Kitob nomi: ").strip().lower()
    topilgan = [k for k in kitoblar if so_rov in k["nom"].lower()]
    if not topilgan:
        print("Kitob topilmadi.")
        return
    for kitob in topilgan:
        kitob_chiqarish(kitob)


def kategoriya_boyicha_filtrlash(kitoblar):
    kategoriya = input("Kategoriya: ").strip().lower()
    topilgan = [k for k in kitoblar if k["kategoriya"].lower() == kategoriya]
    if not topilgan:
        print("Bu kategoriyada kitob topilmadi.")
        return
    for kitob in topilgan:
        kitob_chiqarish(kitob)


def eng_kop_oqilgan_kitob(kitoblar):
    if not kitoblar:
        print("Kitoblar yo'q.")
        return
    kitob = max(kitoblar, key=lambda k: k["oqilgan"])
    print("Eng ko'p o'qilgan kitob:")
    print(f"{kitob['nom']} — {kitob['oqilgan']} marta")


def grafik_chiqarish(kitoblar):
    if not kitoblar:
        print("Grafik uchun ma'lumot yo'q.")
        return
    yigindi = {}
    for kitob in kitoblar:
        yigindi[kitob["kategoriya"]] = (
            yigindi.get(kitob["kategoriya"], 0) + kitob["oqilgan"]
        )

    plt.figure(figsize=(8, 5))
    plt.bar(yigindi.keys(), yigindi.values(), color="tab:blue")
    plt.title("Kategoriyalar bo'yicha o'qilganlik soni")
    plt.xlabel("Kategoriyalar")
    plt.ylabel("O'qilgan (marta)")
    plt.tight_layout()
    plt.show()


def menyu():
    print("\n1. Kitoblarni ko'rish")
    print("2. Kitob qidirish")
    print("3. Kategoriya bo'yicha filtrlash")
    print("4. Eng ko'p o'qilgan kitob")
    print("5. Grafik chiqarish")
    print("6. Kitob qo'shish")
    print("0. Chiqish")


def main():
    kitoblar = kitoblarni_yuklash()

    while True:
        menyu()
        tanlov = input("Tanlov: ").strip()

        if tanlov == "1":
            kitoblarni_korish(kitoblar)
        elif tanlov == "2":
            kitob_qidirish(kitoblar)
        elif tanlov == "3":
            kategoriya_boyicha_filtrlash(kitoblar)
        elif tanlov == "4":
            eng_kop_oqilgan_kitob(kitoblar)
        elif tanlov == "5":
            grafik_chiqarish(kitoblar)
        elif tanlov == "6":
            kitob_qoshish(kitoblar)
        elif tanlov == "0":
            print("Dastur tugadi.")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")


if __name__ == "__main__":
    main()