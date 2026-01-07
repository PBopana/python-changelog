def say_hello(name: str) -> str:
    """
    Say hello to a person.

    :param name: Name of the person to say hello to
    """
    if not name:
        return "Hello!"
    return f"Hello, {name}!"
