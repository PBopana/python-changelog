def say_hello(name: str) -> str:
    """
    Say hello to a person.

    :param name: Name of the person to say hello to
    """
    if not name:
        return "Hello!"
    return f"Hello, {name}!"

def greet_formal(name: str) -> str:
    if not name:
        return "Good day."
    return f"Good day, {name}."

