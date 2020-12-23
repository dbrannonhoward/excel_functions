import random


def get_random_one_digit_number() -> int:
    random_number = random.randint(0, 9)
    return random_number


def get_random_two_digit_number() -> int:
    random_number = random.randint(10, 99)
    return random_number


def get_random_three_digit_number() -> int:
    random_number = random.randint(100, 999)
    return random_number
