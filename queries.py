def query_name() -> str:
    return input("Enter your name\n").strip()

def query_system() -> str:
    return input("Which system do you use?\n").strip()

def query_language() -> str:
    return input("Which language do you speak?\n").strip().lower()
