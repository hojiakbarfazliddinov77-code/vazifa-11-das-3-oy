fayllar = ["Hisobot 2026.pdf", "profil rasmi.jpg",
           "video.mp4", "jadval.xlsx", "diagramma.png"]

ruxsat_etilgan = (".pdf", ".jpg", ".png")

yaroqli = []
yaroqsiz = []

for fayl in fayllar:
    if fayl.lower().endswith(ruxsat_etilgan):
        yaroqli.append(fayl.replace(" ", "_"))
    else:
        yaroqsiz.append(fayl)

print("Yaroqli:")
for fayl in yaroqli:
    print(fayl)

print("\nYaroqsiz:")
for fayl in yaroqsiz:
    print(fayl)