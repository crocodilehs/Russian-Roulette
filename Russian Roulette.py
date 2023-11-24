import random
import os

def russian_roulette():
    target_number = random.randint(1, 6)
    guessed_numbers = set()
    print("GAME START!")
    while True:
        os.system('pause')
        user_number = random.randint(1, 6)
        while user_number in guessed_numbers:
            user_number = random.randint(1, 6)       
        if user_number == target_number:
            print("Bang!!")
            os.system("shutdown /s /t 1")
            break
        else:
            print("You Survived")
            guessed_numbers.add(user_number)


if __name__ == "__main__":
    russian_roulette()