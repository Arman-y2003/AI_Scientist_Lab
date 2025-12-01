import numpy as np
import matplotlib.pyplot as plt
import os
import json

# خواندن مسیرهای خروجی از JSON متناظر
with open("tasks/task2.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

results_path = cfg["outputs"]["results"]
report_path = cfg["outputs"]["report"]
plot_path = cfg["outputs"]["plot"]

# ساخت پوشه خروجی
os.makedirs(os.path.dirname(results_path), exist_ok=True)

# تولید داده و محاسبات
data = np.random.normal(0, 1, 1000)
mu = float(np.mean(data))
sigma = float(np.std(data))

# ذخیره نتایج
with open(results_path, "w", encoding="utf-8") as f:
    f.write(f"میانگین: {mu}\n")
    f.write(f"انحراف معیار: {sigma}\n")
    f.write(f"تعداد نمونه‌ها: {len(data)}\n")

with open(report_path, "w", encoding="utf-8") as f:
    f.write("# گزارش آزمایش دوم\n")
    f.write(f"- میانگین: {mu}\n")
    f.write(f"- انحراف معیار: {sigma}\n")
    f.write("- داده‌ها: نرمال با میانگین 0 و واریانس 1\n")

# ذخیره نمودار
plt.figure(figsize=(6,4))
plt.hist(data, bins=30, color="skyblue", edgecolor="black")
plt.title("Histogram of Normal Distribution")
plt.tight_layout()
plt.savefig(plot_path)
plt.close()
