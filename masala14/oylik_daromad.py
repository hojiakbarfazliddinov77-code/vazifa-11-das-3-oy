import matplotlib.pyplot as plt

oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
daromad = [12, 15, 11, 19, 22, 18]
plt.figure(figsize=(8, 5))
plt.plot(oylar, daromad, marker="o", color="tab:blue")
plt.title("Oylik daromad dinamikasi")
plt.xlabel("Oylar")
plt.ylabel("Daromad (mln so'm)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()