import re

def check_length(password):
    """Check if password meets the length criteria."""
    return len(password) >= 8

def check_lowercase(password):
    """Check if password contains lowercase letters."""
    return any(char.islower() for char in password)

def check_uppercase(password):
    """Check if password contains uppercase letters."""
    return any(char.isupper() for char in password)

def check_digit(password):
    """Check if password contains digits."""
    return any(char.isdigit() for char in password)

def check_special_character(password):
    """Check if password contains special characters."""
    special_characters = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    return special_characters.search(password) is not None

def assess_password_strength(password):
    """Assess the strength of the password based on various criteria."""
    strength = 0

    if check_length(password):
        strength += 1
    if check_lowercase(password):
        strength += 1
    if check_uppercase(password):
        strength += 1
    if check_digit(password):
        strength += 1
    if check_special_character(password):
        strength += 1

    return strength

def main():
    while True:
        password = input("Enter a password to assess its strength (or 'quit' to exit): ")

        if password.lower() == 'quit':
            print("Exiting...")
            break

        strength = assess_password_strength(password)

        if strength == 5:
            print("Password is very strong.")
        elif strength >= 3:
            print("Password is strong.")
        elif strength >= 2:
            print("Password is moderate.")
        elif strength >= 1:
            print("Password is weak. Please consider adding more complexity.")
        else:
            print("Password does not meet minimum criteria. Please make it longer and include a mix of characters.")

if __name__ == "__main__":
    main()
