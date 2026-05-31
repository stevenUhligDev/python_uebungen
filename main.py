        
from collections.abc import Callable

def query_name() -> str:
    return input("Enter your name\n").strip()

def query_system() -> str:
    return input("Which system do you use?\n").strip()

def query_language() -> str:
    return input("Which language do you speak?\n").strip().lower()

def get_valid_input(query_function: Callable[[], str]) -> str:
    while True:
        user_input = query_function()
        if user_input:
            return user_input
        print("Empty input\n")

def create_greeting(name: str, system: str, language: str) -> str:
    match language:
        case "german" | "deutsch":
            return f"Hallo {name}, dein Python läuft auf dem {system}."
        case "english":
            return f"Hello {name}, your Python runs on a {system}."    
        case _:
            return f"{language} not supported"
  

if __name__ == "__main__":
    name = get_valid_input(query_name)    
    system = get_valid_input(query_system)
    language = get_valid_input(query_language)

    message = create_greeting(name, system, language)
    print(message)

    print("Program ends")
    
