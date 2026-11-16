import re
from collections import Counter

matn = "Python dasturlash qiziqarli. Python imkoniyatlari keng."

sozlar = re.findall(r"\w+", matn.lower())

# 1. So'zlar soni
print("So'zlar soni:", len(sozlar))

print("Eng uzun so'z:", max(sozlar, key=len))

harflar = [h for h in matn.lower() if h.isalpha()]
eng_kop_harf = Counter(harflar).most_common(1)[0][0]
print("Eng ko'p uchragan harf:", eng_kop_harf)

sanoq = Counter(sozlar)
noyob = [s for s in sozlar if sanoq[s] == 1]
print("Takrorlanmaydigan so'zlar:", ", ".join(noyob))