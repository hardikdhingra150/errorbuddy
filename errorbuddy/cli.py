import sys
import os
from .explainer import explain


def find_file(filename):
    # 1️⃣ Check current directory
    if os.path.exists(filename):
        return filename

    # 2️⃣ Search in subdirectories
    for root, dirs, files in os.walk(os.getcwd()):
        if filename in files:
            return os.path.join(root, filename)

    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: errorbuddy <file.py>")
        return

    file_input = sys.argv[1]

    file_path = find_file(file_input)

    if not file_path:
        print(f"❌ File not found: {file_input}")
        print("💡 Tip: Make sure file exists or check spelling")
        return

    try:
        with open(file_path) as f:
            code = f.read()
        exec(code, {})
    except Exception as e:
        explain(e)