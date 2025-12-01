import numpy as np
import os

# تولید داده تصادفی
data = np.random.rand(10)
mean = np.mean(data)
std = np.std(data)

# مسیر خروجی
os.makedirs("runs/0001", exist_ok=True)

# ذخیره نتایج
with open("runs/0001/results.txt", "w", encoding="utf-8") as f:
    f.write("نمونه داده:\n")
    f.write(str(data) + "\n")
    f.write("میانگین: " + str(mean) + "\n")
    f.write("انحراف معیار: " + str(std) + "\n")

# گزارش Markdown
with open("runs/0001/report.md", "w", encoding="utf-8") as f:
    f.write("# آزمایش 0001\n")
    f.write("این آزمایش شامل تولید داده تصادفی و محاسبهٔ میانگین و انحراف معیار بود.\n\n")
    f.write(f"- میانگین: {mean}\n")
    f.write(f"- انحراف معیار: {std}\n")
