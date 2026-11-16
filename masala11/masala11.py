import json

FAYL = "sozlamalar.json"

try:
    with open(FAYL, "r", encoding="utf-8") as f:
        sozlamalar = json.load(f)
except FileNotFoundError:
    print(f"Xatolik: {FAYL} fayli topilmadi.")
    raise SystemExit
except json.JSONDecodeError:
    print(f"Xatolik: {FAYL} fayli noto'g'ri formatda.")
    raise SystemExit

while True:
    mavzu = input("Mavzu (light/dark): ").strip().lower()
    if mavzu in ("light", "dark"):
        break
    print("Iltimos, faqat 'light' yoki 'dark' kiriting.")

while True:
    javob = input("Bildirishnoma (ha/yo'q): ").strip().lower()
    if javob in ("ha", "yo'q"):
        break
    print("Iltimos, faqat 'ha' yoki 'yo'q' kiriting.")

sozlamalar["mavzu"] = mavzu
sozlamalar["bildirishnoma"] = (javob == "ha")

with open(FAYL, "w", encoding="utf-8") as f:
    json.dump(sozlamalar, f, indent=2, ensure_ascii=False)

print("Sozlamalar yangilandi.")