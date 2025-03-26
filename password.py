import random
import string
import pyperclip  # To copy password to clipboard

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Generates a secure random password based on user preferences."""

    # Define character sets
    lower = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    upper = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits if use_digits else ""  # 0123456789
    special_chars = string.punctuation if use_special_chars else ""  # Special symbols

    # Combine character sets
    all_characters = lower + upper + digits + special_chars
    if not all_characters:
        print("Error: No character set selected!")
        return None

    # Generate random password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    # Copy to clipboard
    pyperclip.copy(password)
    print(f"Generated Password: {password} (Copied to Clipboard ✅)")

    return password

# User Input
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        generate_password(length, use_digits, use_special_chars)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
