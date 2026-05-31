name = "Steven"
system = "Raspberry Pi 5"


def create_greeting(name, system):
    message = f"Hallo {name}, dein Python läuft auf dem {system}."
    return message
    
    
message = create_greeting(name, system)
print(message)