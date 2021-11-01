import random
import timeit

bit_list = [2, 4, 8]
run = 30


def random_bit_pattern(size: int):
    bit_pattern = ""
    for i in range(size):
        random_bit = random.random()
        if random_bit > 0.5:
            bit_pattern += "0"
        else:
            bit_pattern += "1"
    return bit_pattern


def goal_guess():
    for i in range(run):
        for j in bit_list:
            run_goal = random_bit_pattern(j)
            solution = random_bit_pattern(j)
            guess = 0
            while run_goal != solution:
                solution = random_bit_pattern(2)
                guess += 1

            print(solution)
            print(run_goal)
            return guess


if __name__ == '__main__':
    print(goal_guess())
