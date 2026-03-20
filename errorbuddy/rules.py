ERROR_RULES = {

    # 🔴 TYPE & VALUE
    "TypeError": {
        "explanation": "You used incompatible data types together.",
        "fix": "Ensure all operands are of compatible types or convert them.",
        "example": "int('5') + 10",
        "hint": "Check if you're mixing int, str, list, etc."
    },

    "ValueError": {
        "explanation": "The value is of correct type but invalid.",
        "fix": "Ensure the value matches the expected format.",
        "example": "int('123')",
        "hint": "Common in int(), float(), or unpacking."
    },

    # 🔴 INDEX / KEY
    "IndexError": {
        "explanation": "Index is out of range.",
        "fix": "Check list length before accessing index.",
        "example": "if i < len(arr): arr[i]"
    },

    "KeyError": {
        "explanation": "Key not found in dictionary.",
        "fix": "Use .get() or check if key exists.",
        "example": "my_dict.get('key')"
    },

    # 🔴 NAME / ATTRIBUTE
    "NameError": {
        "explanation": "Variable or function is not defined.",
        "fix": "Define it before use or check spelling.",
        "example": "x = 10"
    },

    "AttributeError": {
        "explanation": "Object doesn't have this method/attribute.",
        "fix": "Check object type and available methods.",
        "example": "'hello'.upper()"
    },

    # 🔴 IMPORT
    "ImportError": {
        "explanation": "Failed to import module.",
        "fix": "Check module name or installation.",
        "example": "pip install package_name"
    },

    "ModuleNotFoundError": {
        "explanation": "Module not installed.",
        "fix": "Install using pip.",
        "example": "pip install requests"
    },

    # 🔴 FILE HANDLING
    "FileNotFoundError": {
        "explanation": "File does not exist at given path.",
        "fix": "Check file path or working directory.",
        "example": "open('file.txt')"
    },

    "PermissionError": {
        "explanation": "No permission to access file.",
        "fix": "Change permissions or run with correct access.",
        "example": "chmod +r file.txt"
    },

    "IsADirectoryError": {
        "explanation": "Tried to open a directory as file.",
        "fix": "Provide correct file path.",
        "example": "open('file.txt')"
    },

    # 🔴 MATH
    "ZeroDivisionError": {
        "explanation": "Division by zero is not allowed.",
        "fix": "Ensure denominator is not zero.",
        "example": "if b != 0: a / b"
    },

    "OverflowError": {
        "explanation": "Result too large to handle.",
        "fix": "Use smaller values or optimize logic.",
        "example": "math.exp(10)"
    },

    # 🔴 ASSERT / LOGIC
    "AssertionError": {
        "explanation": "Assertion condition failed.",
        "fix": "Check your condition logic.",
        "example": "assert x > 0"
    },

    # 🔴 SYNTAX
    "SyntaxError": {
        "explanation": "Invalid Python syntax.",
        "fix": "Check missing symbols (:, (), '').",
        "example": "if x > 5:"
    },

    "IndentationError": {
        "explanation": "Incorrect indentation.",
        "fix": "Use consistent spacing.",
        "example": "use 4 spaces"
    },

    "TabError": {
        "explanation": "Mixed tabs and spaces.",
        "fix": "Use only spaces.",
        "example": "convert tabs to spaces"
    },

    # 🔴 ENCODING
    "UnicodeDecodeError": {
        "explanation": "Failed to decode text.",
        "fix": "Specify correct encoding.",
        "example": "open(file, encoding='utf-8')"
    },

    "UnicodeEncodeError": {
        "explanation": "Failed to encode text.",
        "fix": "Use supported encoding.",
        "example": "text.encode('utf-8')"
    },

    # 🔴 MEMORY / RECURSION
    "MemoryError": {
        "explanation": "Program ran out of memory.",
        "fix": "Use generators or optimize data.",
        "example": "use yield instead of list"
    },

    "RecursionError": {
        "explanation": "Too many recursive calls.",
        "fix": "Add base condition.",
        "example": "if n == 0: return"
    },

    # 🔴 RUNTIME
    "TimeoutError": {
        "explanation": "Operation took too long.",
        "fix": "Optimize logic or increase timeout.",
        "example": "set timeout parameter"
    },

    "RuntimeError": {
        "explanation": "Unexpected runtime issue.",
        "fix": "Check logic and flow.",
        "example": "review stack trace"
    }
}