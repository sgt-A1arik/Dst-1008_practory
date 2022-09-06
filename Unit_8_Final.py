#@title Текст заголовка по умолчанию
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток
    """

    count = 0  # количество попыток угадывания   
    number = np.random.randint(1, 101)  # загадываем число
    predict_number = np.random.randint(1, 101)

    while True:
        count += 1
        
        if number == predict_number:
            break  # выход из цикла, если угадали
        elif number < predict_number:
            # если предлагаемое число больше заданного,
            predict_number = np.random.randint(number, predict_number)
            # корректируем наше число.
        else:  # если предлагаемое число меньше заданного,
            predict_number = np.random.randint(predict_number+1, number+1)
            # корректируем наше число.   
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
