import string
import random

def generate_password(length, num_passwords):
    """
    Generate random passwords with given length and number.

    :param length: int, the desired length of the password
    :param num_passwords: int, the number of passwords to generate
    :return: list of strings, a list containing the generated passwords
    """

    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    if length < 8:
        print("It is recommended to have a minimum password length of 8 characters.")
        
    if num_passwords < 1:
        print("Number of passwords to generate should be at least 1.")
        return []

    passwords = []

    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)

    return passwords


if __name__== "__main__":
    # Example usage
    length = int(input("Enter the desired password length: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    generated_passwords = generate_password(length, num_passwords)

    print("\nGenerated Passwords:")
    for password in generated_passwords:
        print(password)