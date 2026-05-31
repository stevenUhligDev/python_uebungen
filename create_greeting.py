def create_greeting(name: str, system: str, language: str) -> str:
    match language:
        case "german" | "deutsch":
            return f"Hallo {name}, dein Python läuft auf dem {system}."
        case "english":
            return f"Hello {name}, your Python runs on a {system}."    
        case _:
            return f"{language} not supported"