import json
import subprocess
import sys

# فیلتر آرگومان‌های اضافی
args = [a for a in sys.argv[1:] if not a.startswith("-")]
task_file = args[0] if args else "tasks/task1.json"

with open(task_file, "r", encoding="utf-8") as f:
    task = json.load(f)

code_path = f"tasks/{task['code']}"
subprocess.run(["python", code_path], check=True)
