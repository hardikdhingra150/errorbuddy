import sys
import os
from .explainer import explain


# 🔍 Smart file finder (clean + fast)
def find_file(filename):
    # Add .py if missing
    if not filename.endswith(".py"):
        filename += ".py"

    # 1️⃣ Direct path (absolute or relative)
    if os.path.exists(filename):
        return os.path.abspath(filename)

    # 2️⃣ Priority-based search paths
    search_paths = [
        os.getcwd(),                      # highest priority
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Downloads"),
    ]

    found_files = set()  # ✅ removes duplicates

    for base_path in search_paths:
        if not os.path.exists(base_path):
            continue

        for root, dirs, files in os.walk(base_path):
            if filename in files:
                found_files.add(os.path.join(root, filename))

    if not found_files:
        return None

    # 3️⃣ Convert to list
    found_files = list(found_files)

    # 4️⃣ Smart selection (no user input)
    # Prefer closest match (shortest path)
    found_files.sort(key=lambda x: len(x))

    return found_files[0]


# 🚀 CLI ENTRY
def main():
    if len(sys.argv) < 2:
        print("Usage: errorbuddy <file.py>")
        return

    file_input = sys.argv[1]

    file_path = find_file(file_input)

    if not file_path:
        print(f"❌ File not found: {file_input}")
        print("💡 Searched in: current folder, Desktop, Documents, Downloads")
        return

    try:
        with open(file_path, "r") as f:
            code = f.read()

        # Execute safely
        exec_globals = {}
        exec(code, exec_globals)

    except Exception as e:
        explain(e)