natijalar = [
    {"ism": "Aziza", "ball": 82},
    {"ism": "Jasur", "ball": 64},
    {"ism": "Madina", "ball": 91},
    {"ism": "Sardor", "ball": 70}
]

yuqori = list(filter(lambda n: n["ball"] > 70, natijalar))

oshirilgan = list(map(lambda n: round(n["ball"] * 1.1, 1), natijalar))

saralangan = sorted(natijalar, key=lambda n: n["ball"], reverse=True)

print("70 dan yuqori:", ", ".join(n["ism"] for n in yuqori))
print("10% oshirilgan ballar:", oshirilgan)
print("Saralangan:", ", ".join(n["ism"] for n in saralangan))