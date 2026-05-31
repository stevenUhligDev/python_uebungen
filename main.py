

def create_greeting(name, system, language):
    match language:
        case "german":
            message = f"Hallo {name}, dein Python läuft auf dem {system}."
            return message
        case "english":
            message = f"Hello {name}, your Python runs on a {system}."
            return message    
        case _:
            message = f"{language} not supported"
            return message
    
    
name = input("Enter your name \n").strip()
system = input("Which system do you use? \n").strip()
language = input("Which language do you speak? \n").strip().lower()
message = create_greeting(name, system, language)
print(message)