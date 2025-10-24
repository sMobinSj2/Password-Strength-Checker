import pyperclip

def error_handling(pw):
    try:
        validate_password(pw)
        return True
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False

# function to validate password strength
def validate_password(password: str) -> None:
    #check for length
    if len(password) < 8:
        raise ValueError("Password must be at least 8 character.")
    # Checking to not start with number
    elif not password[0].isalpha():
        raise ValueError("Password should't start with number.")
    # Checking to not start with lowercase character
    elif password[0].islower():
        raise ValueError("Password shouldn't start with a lowercase letter.")
    # Checking for symbols
    elif not any(char in "!@#$%^&*()-+" for char in password):
        raise ValueError("Password must contain at least one special symbol (!@#$%^&*()-+).")
    else:
        print("Password strength is good.")
        pyperclip.copy(password)
        print("Password has been copied to clipboard.")

def main():
    is_valid = False
    while not is_valid:
        pw = input("Enter your password: ")
        is_valid = error_handling(pw)

if __name__ == "__main__":
    main()