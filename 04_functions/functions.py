import math


def find_cool_numbers(test=None):
    nums = []
    for n in range(0, 25):
        if test is None:
            nums.append(n)
        elif test(n):
            nums.append(n)
    return nums


def even_nums(n):
    return n % 2 == 0


def thirds_nums(n):
    return n % 3 == 0


#def sort_by_abs(n):
#    return math.fabs(n)


def sorting():
    some_data = [1, 3, -1, 7, 11, -2]
    #some_data.sort(even_nums)
    some_data.sort(key=lambda n:n % 3 == 0)
    print(some_data)


def filter_nums():
    print('Looking for some cool numbers')
    for n in find_cool_numbers(thirds_nums):
        print(n, end=',')


if __name__ == '__main__':
    filter_nums()
    #sorting()
