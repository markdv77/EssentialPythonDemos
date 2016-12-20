def get_fibonacci_numbers():
    # 1, 1, 2, 3, 5, 8, 13, 21....
    current, nxt = 0, 1
    data = []
    while True:
        current, nxt = nxt, nxt+current
        yield current
    return data


def main():
    f = get_fibonacci_numbers()
    for n in f:
        print(n)

    print()
    print('done')


if __name__ == '__main__':
    main()
