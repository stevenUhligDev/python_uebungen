import create_greeting
import get_valid_input
import queries

def main():
    name = get_valid_input.get_valid_input(queries.query_name)    
    system = get_valid_input.get_valid_input(queries.query_system)
    language = get_valid_input.get_valid_input(queries.query_language)
    message = create_greeting.create_greeting(name, system, language)
    print(message)
    print("Program ends")
if __name__ == "__main__":
    main()    
    
