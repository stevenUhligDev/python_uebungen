from collections.abc import Callable


def get_valid_input(query_function: Callable[[], str]) -> str:
    while True:
        user_input = query_function()
        if user_input:
            return user_input
        print("Empty input\n")