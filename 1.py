def return_hello(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


return_hello_execution = return_hello("Jan", "Kowalski")
print(return_hello_execution)
print(type(return_hello_execution))
