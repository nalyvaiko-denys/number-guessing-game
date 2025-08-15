

from game_logic import play_game

def main():
    while True:
        play_game()
        play_again = input("Wanna play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("See you next time.")

if __name__ == "__main__":
    main()