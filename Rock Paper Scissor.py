import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("Rock, Paper, Scissors Game")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == '4':
            print("Thanks for playing! Final Scores:")
            print(f"You: {user_score} - Computer: {computer_score}")
            break

        if user_choice not in ('1', '2', '3'):
            print("Invalid choice. Please enter a valid option.")
            continue

        user_choice = user_choice_map[user_choice]
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score: You ({user_score}) - Computer ({computer_score})\n")

if _name_ == "_main_":
    user_choice_map = {
        '1': 'rock',
        '2': 'paper',
        '3': 'scissors'
    }
    main()