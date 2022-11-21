__all__ = [
    'get_user_input',
    'output_to_user'
]


def get_user_input(message: str):
    return input(message)


def output_to_user(message: str):
    print(message)