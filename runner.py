import json
import subprocess

# خواندن وظیفه
with open("tasks/task1.json", "r", encoding="utf-8") as f:
    task = json.load(f)

# اجرای کد وظیفه
subprocess.run(["python", f"tasks/{task['code']}"])
