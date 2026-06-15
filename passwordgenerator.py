import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            print("Password should be at least 8 characters.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

characters = (
    string.ascii_uppercase +
    string.ascii_lowercase +
    string.digits +
    string.punctuation
)

password = ''.join(random.choice(characters) for _ in range(length))

print("\nGenerated Password:")
print(password)

print("\nPassword generated successfully!")
