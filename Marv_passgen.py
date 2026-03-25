import random
import string

def generate_password(length=12):
    """
    Generate a random password of specified length.
    
    Args:
        length (int): The length of the password to generate. Default is 12.
    
    Returns:
        str: The generated password.
    """
    # Combine all possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    try:
        # Get password length from user
        length = int(input("Enter password length (default 12): ") or 12)
        
        # Generate and display password
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for password length.")
