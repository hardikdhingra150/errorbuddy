from .rules import ERROR_RULES
import traceback
from colorama import Fore, Style


# 🔥 Smart message-based hints
def get_smart_hint(message: str):
    message = message.lower()

    if "unsupported operand" in message:
        return "👉 You're using incompatible types (e.g., int + str). Try type conversion."

    if "list index out of range" in message:
        return "👉 Your index exceeds the list size. Check len(list)."

    if "division by zero" in message:
        return "👉 Denominator cannot be zero."

    if "no module named" in message:
        return "👉 Install the missing module using pip."

    if "cannot unpack" in message:
        return "👉 You may be unpacking the wrong number of values."

    if "expected" in message and "got" in message:
        return "👉 Function arguments mismatch."

    return None


# 🔥 Pretty section printer
def print_section(title, color):
    print(color + f"\n{title}" + Style.RESET_ALL)


def explain(error: Exception, debug: bool = False):
    error_name = type(error).__name__
    message = str(error)

    # 🔍 Extract traceback
    tb = traceback.extract_tb(error.__traceback__)
    last_trace = tb[-1] if tb else None

    # 🔴 Header
    print(Fore.RED + f"\n🚨 ERROR: {error_name}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"📍 Message: {message}" + Style.RESET_ALL)

    # 🔵 File + Line Info
    if last_trace:
        print(Fore.BLUE + f"\n📂 File: {last_trace.filename}" + Style.RESET_ALL)
        print(Fore.BLUE + f"📌 Line: {last_trace.lineno}" + Style.RESET_ALL)

        if last_trace.line:
            print(Fore.BLUE + f"👉 Code: {last_trace.line.strip()}" + Style.RESET_ALL)

    # 📚 Rule-based explanation
    rule = ERROR_RULES.get(error_name)

    if rule:
        print_section("🧠 What happened?", Fore.CYAN)
        print(rule.get("explanation", ""))

        print_section("🛠️ How to fix it?", Fore.GREEN)
        print(rule.get("fix", ""))

        print_section("✅ Example:", Fore.MAGENTA)
        print(rule.get("example", ""))

        # Optional hint
        if "hint" in rule:
            print_section("💡 Tip:", Fore.WHITE)
            print(rule["hint"])

    else:
        print_section("🤔 Unknown error", Fore.WHITE)
        print("📌 Try checking documentation or searching the error.")

    # 🧠 Smart dynamic hint
    hint = get_smart_hint(message)
    if hint:
        print_section("💡 Smart Hint:", Fore.LIGHTWHITE_EX)
        print(hint)

    # 🧾 Optional debug traceback
    if debug:
        print(Fore.LIGHTBLACK_EX + "\n🔍 Full Traceback:" + Style.RESET_ALL)
        traceback.print_exception(type(error), error, error.__traceback__)

    print(Fore.LIGHTBLACK_EX + "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + Style.RESET_ALL)