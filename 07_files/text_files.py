import os


def main():
    data = []

    root_path = os.path.abspath('.')
    folder = 'data'
    file = 'Sacramentorealestatetransactions.csv'
    filename = os.path.join(root_path, folder, file)

    print('Loading from {}'.format(filename))

    with open(filename, 'r') as fin:
        first_line = fin.readline()
        header = first_line.strip().split(',')
        for purchase in fin:
            line_data = purchase.strip().split(',')
            d = dict()
            for idx, name in enumerate(header):
                d[name] = line_data[idx]
            data.append(d)

    data.sort(key=lambda p: -float(p['price']))

    for d in data[:5]:
        print(d)


if __name__ == '__main__':
    main()
