name = "Steven"
system = "Raspberry Pi 5"
language_de = "de"
language_en = "en"


def create_greeting(name, system, language):
    match language:
        case "de":
            message = f"Hallo {name}, dein Python läuft auf dem {system}."
            return message
        case "en":
            message = f"Hello {name}, your Python runs on a {system}."
            return message    
        case _:
            message = f"{language} not supported"
            return message
    
    

message = create_greeting(name, system, "nl")
print(message)