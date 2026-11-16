import matplotlib.pyplot as plt

buyurtma_qiymatlari = [50, 75, 80, 120, 150, 150, 180, 220, 250, 300]

plt.figure(figsize=(8, 5))
plt.hist(buyurtma_qiymatlari, bins=5, color="tab:purple", edgecolor="black")
plt.title("Buyurtma qiymatlari taqsimoti")
plt.xlabel("Buyurtma qiymati")
plt.ylabel("Buyurtmalar soni")
plt.tight_layout()
plt.show()