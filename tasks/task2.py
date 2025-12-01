import numpy as np
import matplotlib.pyplot as plt
import os
import json

# خواندن تنظیمات خروجی از فایل وظیفه
with open("tasks/task2.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

# مسیرهای خروجی
results_path = cfg["outputs"]["results"]
report_path = cfg["outputs"]["report"]
plot_path = cfg["outputs"]["plot"]

# ساخت پوشهٔ خروجی اگر وجود نداشت
os.makedirs(os.path.dirname(results_path), exist_ok=True)

# تولید داده نرمال
data = np.random.normal(loc=0, scale=1, size=1000)
mu = float(np.mean(data))
sigma = float(np.std(data))

# ذخیرهٔ نتایج عددی
with open(results_path, "w", encoding="utf-8") as f:
    f.write(f"میانگین: {mu}\n")
    f.write(f"انحراف معیار: {sigma}\n")
    f.write(f"تعداد نمونه‌ها: {len(data)}\n")

# ذخیرهٔ گزارش متنی
with open(report_path, "w", encoding="utf-8") as f:
    f.write("# گزارش آزمایش دوم\n")
    f.write(f"- میانگین داده‌ها: {mu}\n")
    f.write(f"- انحراف معیار داده‌ها: {sigma}\n")
    f.write("- نوع داده: توزیع نرمال با میانگین صفر و واریانس یک\n")

# رسم و ذخیرهٔ نمودار هیستوگرام
plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color="skyblue", edgecolor="black")
plt.title("Histogram of Normal Distribution")
plt.xlabel("مقدار")
plt.ylabel("تعداد")
plt.tight_layout()
plt.savefig(plot_path)
plt.close()
