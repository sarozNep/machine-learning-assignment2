from matplotlib import pyplot
import random
import timeit

sizes = [2, 4, 8, 12, 16]


def random_bit(size: int):
    bit_pattern = ""
    for i in range(size):
        rnd = random.random()
        if rnd > 0.5:
            bit_pattern += "0"
        else:
            bit_pattern += "1"
    return bit_pattern


def test_for_different_size():
    total_attempts = []
    total_time = []
    total_attempts_avg = []
    total_time_avg = []
    for x in sizes:
        res = []

        for y in range(30):
            correct = random_bit(x)
            attempts_num = 1
            time = timeit.default_timer()
            attempt = random_bit(x)

            while attempt != correct:
                attempts_num += 1
                attempt = random_bit(len(correct))

            total_time = timeit.default_timer() - time
            res_size = (attempts_num, total_time)
            res.append(res_size)

        attempts_avg = 0
        time_avg = 0
        for z in res:
            attempts_avg += z[0]
            time_avg += z[1]

        attempts_avg /= 30
        time_avg /= 30

        total_attempts_avg.append(attempts_avg)
        total_time_avg.append(time_avg)

    return total_attempts_avg, total_time_avg


if __name__ == '__main__':
    res = test_for_different_size()

    pyplot.subplot(2, 1, 1)
    pyplot.plot(sizes, res[0])
    pyplot.xlabel("pattern_size")
    pyplot.ylabel("average_attempts")

    pyplot.subplot(2, 1, 2)
    pyplot.plot(sizes, res[1])
    pyplot.xlabel("pattern_size")
    pyplot.ylabel("run_time")

    pyplot.tight_layout()
    pyplot.show()