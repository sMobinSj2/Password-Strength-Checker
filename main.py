import pyperclip

# function to handle errors during password validation
def pw_validation_check(pw):
    try:
        pw_strength_check(pw)
        return True
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return False
   

# function to validate password strength
def pw_strength_check(password: str) -> None:
    
    #check for length of the password
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")
    
    # Checking password to have at least one number
    elif not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    
    # Checking to not start with number
    elif not password[0].isalpha():
        raise ValueError("Password must start with a letter.")
    
    # Checking the password to have at least one uppercase letter
    elif not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    
    # Checking the password to have at least one lowercase letter
    elif not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    
    # Checking for symbols
    elif not any(char in "!@#$%^&*()-+" for char in password):
        raise ValueError("Password must contain at least one special symbol (!@#$%^&*()-+).")
        
    print("Password strength is good.")
    
    try:
        pyperclip.copy(password)
    except pyperclip.PyperclipException as pyex:
        print(f"Warning: could not copy password to clipboard ({pyex}).")
    else:
        print("Password has been copied to clipboard.")

def main():
    is_valid = False
    # Loop until a valid password is entered that meets all criteria
    while not is_valid:
        pw = input("Enter your password: ")
        is_valid = pw_validation_check(pw)

if __name__ == "__main__":
    main()