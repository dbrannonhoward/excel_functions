import random
import time


class Coin:
    def __init__(self):
        self.state = None
        self.min = 0
        self.threshold = 50
        self.max = 100
        self.flip()

    def change_state(self):
        wait_one_second()
        try:
            if self.state is None:
                self.flip()
            if self.state:
                self.state = False
                return
            self.state = True
            return
        except CoinError as uh_oh:
            print('uh oh {}'.format(uh_oh))

    def choose_starting_state(self):
        wait_one_second()
        print('{} has no state, choosing starting state'.format(self.__class__.__name__))
        try:
            a_few_flips = list()
            for flip_number in range(self.max):
                a_few_flips.append(int(random.randint(self.min, self.max)))
            if average_of_list(a_few_flips) < self.threshold:
                self.state = True
        except CoinError as uh_oh:
            print('uh oh {}'.format(uh_oh))

    def flip(self):
        wait_one_second()
        try:
            if self.state is None:
                self.choose_starting_state()
                return
            if random.randint(self.min, self.max) < self.threshold:
                self.change_state()
                return
        except CoinError as uh_oh:
            print('uh oh {}'.format(uh_oh))


def average_of_list(list_of_int: list) -> int:
    sum_of_list = 0
    for number in list_of_int:
        sum_of_list += number
    return int(sum_of_list / len(list_of_int))


def wait_one_second():
    time.sleep(1)


class CoinError(Exception):
    def __init__(self):
        super().__init__()
