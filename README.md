# PassWord_generator

# User Input:
The user is prompted to enter the desired password length (between 8 and 12).
They also specify how many letters, symbols, and digits they want in the password.
Password Generation:
The generate_password function creates a list of characters based on the user’s input.
It randomly selects letters from both uppercase and lowercase alphabets, digits (0-9), and symbols (e.g., !, @, #, $, %, ^, &, *, (, ), _).
The selected characters are shuffled randomly to create the final password.
# Validation:
The get_user_input function ensures that the user provides valid input:
If the password length is outside the range [8, 12], it displays an error message.
If the user enters an invalid input (not a number), it prompts them to enter a valid number.
It also checks if the total length of letters, symbols, and digits matches the specified password length.
# Display:
The display_password function shows the generated password to the user.
# Main Loop:
The main loop allows the user to create multiple passwords or exit the program.
Overall, this code provides a simple command-line interface for generating passwords with specific characteristics. You can run this script, and it will interactively prompt you for input to create passwords
