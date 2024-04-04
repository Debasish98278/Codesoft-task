import random
def check_winner(user_choice, Debasish_choice):
    if user_choice == Debasish_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and Debasish_choice == 'scissors') or \
         (user_choice == 'scissors' and Debasish_choice == 'paper') or \
         (user_choice == 'paper' and Debasish_choice == 'rock'):
        return "You win!"
    else:
        return "Debasish wins!"
def play_time():
    user_choice = input("Choose any one (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose any one (rock, paper, scissors).")
        user_choice = input("Choose any one (rock, paper, scissors): ").lower()
    Debasish_choice = random.choice(['rock', 'paper', 'scissors'])
    print("You chose:", user_choice)
    print("Debasish chose:", Debasish_choice)
    print(check_winner(user_choice, Debasish_choice))
def main():
    print("Welcome to Rock-Paper-Scissors Game! with Debasish")
    play_time()
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing with Debasish.")
            print("Please, visit me again")
            break
        play_time()
if __name__ == "__main__":
    main()