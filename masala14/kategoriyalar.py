import matplotlib.pyplot as plt

kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
savdo = [35, 20, 45]

plt.figure(figsize=(8, 5))
plt.bar(kategoriyalar, savdo, color=["tab:blue", "tab:orange", "tab:green"])
plt.title("Kategoriyalar savdosi")
plt.xlabel("Kategoriyalar")
plt.ylabel("Savdo (dona)")
plt.tight_layout()
plt.show()