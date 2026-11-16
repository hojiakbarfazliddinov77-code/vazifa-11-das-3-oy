shaharlar = {"A": (0, 0), "B": (3, 4), "C": (6, 0)}


def masofa(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


nomlar = list(shaharlar.keys())

eng_uzoq_juft = ""
eng_uzoq_masofa = 0

for i in range(len(nomlar)):
    for j in range(i + 1, len(nomlar)):
        a = nomlar[i]
        b = nomlar[j]
        m = masofa(shaharlar[a], shaharlar[b])
        print(a, "va", b + ":", m)

        if m > eng_uzoq_masofa:
            eng_uzoq_masofa = m
            eng_uzoq_juft = a + " - " + b

print("Eng uzoq yo'nalish:", eng_uzoq_juft, "(" + str(eng_uzoq_masofa) + ")")