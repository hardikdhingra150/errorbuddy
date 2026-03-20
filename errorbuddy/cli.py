import sys
import os
from .explainer import explain


# 🔍 Smart file finder
def find_file(filename):
    # Add .py if missing
    if not filename.endswith(".py"):
        filename += ".py"

    # 1️⃣ Direct path (absolute or relative)
    if os.path.exists(filename):
        return os.path.abspath(filename)

    # 2️⃣ Search locations
    search_paths = [
        os.getcwd(),
        os.path.expanduser("~/Desktop"),
        os.path.expanduser("~/Documents"),
        os.path.expanduser("~/Downloads"),
    ]

    matches = []

    for base_path in search_paths:
        if not os.path.exists(base_path):
            continue

        for root, dirs, files in os.walk(base_path):
            if filename in files:
                matches.append(os.path.join(root, filename))

    # 3️⃣ Handle results
    if len(matches) == 1:
        return matches[0]

    elif len(matches) > 1:
        print(f"⚠️ Multiple files found for '{filename}':")
        for i, path in enumerate(matches, 1):
            print(f"{i}. {path}")

        try:
            choice = int(input("Select file number: "))
            return matches[choice - 1]
        except:
            print("❌ Invalid choice.")
            return None

    return None


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