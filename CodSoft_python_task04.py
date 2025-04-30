import random

user_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']
beats = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

print("Welcome to Rock-Paper-Scissors Game!")
print("Choose rock, paper, or scissors to play against the computer. Good luck!\n")

while True:
    # Get and validate user input
    while True:
        user_choice = input("Your choice (rock/paper/scissors): ").lower()
        if user_choice in choices:
            break
        print("Invalid choice. Please try again.")
    
    # Generate computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the result
    if user_choice == computer_choice:
        result = 'tie'
    elif beats[user_choice] == computer_choice:
        result = 'user'
    else:
        result = 'computer'
    
    # Display choices and result
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        user_score += 1
        print("You win this round!")
    else:
        computer_score += 1
        print("Computer wins this round!")
    
    # Display current scores
    print(f"\nScore - You: {user_score} | Computer: {computer_score}")
    
    # Ask to play again
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again not in ['yes', 'y']:
        print("\nThank you for playing! Final Scores:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
    print("\n" + "-"*30 + "\n")