import numpy as np
import matplotlib.pyplot as plt
import os

# تولید داده نرمال
data = np.random.normal(0, 1, 100)
mu = np.mean(data)
sigma = np.std(data)

# ساخت پوشه خروجی
os.makedirs("runs/0002", exist_ok=True)

# ذخیره نتایج
with open("runs/0002/results.txt", "w", encoding="utf-8") as f:
    f.write("میانگین: " + str(mu) + "\n")
    f.write("انحراف معیار: " + str(sigma) + "\n")

# ذخیره گزارش
with open("runs/0002/report.md", "w", encoding="utf-8") as f:
    f.write("# آزمایش 0002\n")
    f.write(f"- میانگین: {mu}\n")
    f.write(f"- انحراف معیار: {sigma}\n")

# رسم نمودار هیستوگرام
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram of Normal Distribution")
plt.savefig("runs/0002/histogram.png")
plt.close()
