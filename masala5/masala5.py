tadbir_1 = {"Ali", "Vali", "Sami", "Lola"}
tadbir_2 = {"Ali", "Sami", "Nodir"}
tadbir_3 = {"Ali", "Lola", "Nodir"}

tadbirlar = [tadbir_1, tadbir_2, tadbir_3]

barchasida = tadbir_1 & tadbir_2 & tadbir_3

sanoq = {}
for t in tadbirlar:
    for ism in t:
        sanoq[ism] = sanoq.get(ism, 0) + 1

# Faqat bittasida
faqat_bitta = {ism for ism, s in sanoq.items() if s == 1}

kamida_ikkita = {ism for ism, s in sanoq.items() if s >= 2}

print("Barcha tadbirlarda:", ", ".join(sorted(barchasida)))
print("Faqat bitta tadbirda:", ", ".join(sorted(faqat_bitta)))
print("Kamida ikkita tadbirda:", ", ".join(sorted(kamida_ikkita)))