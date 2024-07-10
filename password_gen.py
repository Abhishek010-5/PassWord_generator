from pywebio.input import *
from pywebio.output import *
import random

def generate_password(letters, numbers, symbols):
    """Generate a password with the given characteristics"""
    password_chars = []
    password_chars.extend(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(letters))
    password_chars.extend(random.choice('0123456789') for _ in range(numbers))
    password_chars.extend(random.choice('!@#$%^&*()_+') for _ in range(symbols))
    random.shuffle(password_chars)
    return ''.join(password_chars)

def display_password(password):
    """Display the generated password"""
    put_text(f'This is the password -> {password}')

def get_user_input():
    """Get user input for password generation"""
    while True:
        try:
            password_length = input("Enter the password length between 8 to 12", NUMBER)
            if password_length < 8 or password_length > 12:
                put_text("Password length should be between 8 and 12")
                continue
            break
        except ValueError:
            put_text("Invalid input. Please enter a number.")
    
    letters = input("Enter how many letters you need in password", NUMBER)
    symbols = input("Enter how many symbols you need in password", NUMBER)
    numbers = input("Enter how many digits you need in password", NUMBER)
    
    total_length = letters + symbols + numbers
    if total_length != password_length:
        put_text("You entered more numbers than the password length")
        return None
    
    return letters, numbers, symbols

def main():
    put_text("Password Generator")
    while True:
        user_choice = select("Do you want to create a password?", ["Yes", "No"])
        if user_choice == 'Yes':
            user_input = get_user_input()
            if user_input:
                password = generate_password(*user_input)
                display_password(password)
        else:
            put_text("Exited")
            break

if __name__ == '__main__':
    main()