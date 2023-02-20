#functions with outputs

def format_name():
    first_name = input("What's your first name?")
    last_name = input("What's your last name?")
    name = f"Your name is {first_name} {last_name}"
    return name.title()

print(format_name())