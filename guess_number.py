import random

def play_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100, попробуйте угадать.")

    number_to_guess = random.randint(1, 100)
    
    attempts = 0

    while True:
        try:
            user_guess = int(input("Введите ваше предположение: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Слишком мало! Попробуйте еще раз.")
            elif user_guess > number_to_guess:
                print("Слишком много! Попробуйте еще раз.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

play_game()
