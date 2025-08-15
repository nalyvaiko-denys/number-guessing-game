import random


def play_game():
    secret_number = random.randint(1, 10)
    print("\nI'm thinking of a number between 1 and 10. Let's see if you can nail it!")

    guess = 0
    guess_count = 0
    max_tries = 5

    while guess != secret_number and guess_count < max_tries:
        try:
            guess_text = input("What's your best shot? ")
            guess = int(guess_text)
            guess_count += 1

            if guess == secret_number:
                print(
                    f"You nailed it! The secret number was {secret_number}. And you did it in just {guess_count} tries!")
            elif guess_count < max_tries:
                if guess < secret_number:
                    print("A bit too low. Go higher!")
                else:
                    print("Way too high. Come back down!")
            else:
                pass
        except ValueError:
            print("Nah, that's not a number. Try again!")

    if guess != secret_number:
        print(f"Not today. The secret number was {secret_number}.")