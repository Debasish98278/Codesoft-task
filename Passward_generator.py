import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to Debasish's Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Length must be a positive integer.")
        return
    password = generate_password(length)
    print("Your generated password is:", password)
    print("Thanks for using Debasish's Password Generator.")
    print("Please, visit me again")
if __name__ == "__main__":
    main()