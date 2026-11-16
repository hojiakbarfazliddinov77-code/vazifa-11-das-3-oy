def bolish(a, b):
    assert isinstance(a, (int, float)), "a son bo'lishi kerak"
    assert isinstance(b, (int, float)), "b son bo'lishi kerak"
    assert b != 0, "Nolga bo'lish mumkin emas."
    return a / b

try:
    son1 = float(input("Birinchi son: "))
    son2 = float(input("Ikkinchi son: "))
    natija = bolish(son1, son2)
    print("Natija:", natija)
except ValueError:
    print("Xatolik: Faqat son kiriting.")
except (ZeroDivisionError, AssertionError) as xato:
    print(f"Xatolik: {xato}")
finally:
    print("Dastur ishlashda davom etmoqda.")