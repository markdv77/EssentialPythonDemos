#from calculator.sci_calc import ScientificCalculator
from calculator import ScientificCalculator, Graph


def main():
    c = ScientificCalculator()
    print('Sum of {} and {} is {}'.format(5, 8, c.add(5, 8)))

    g = Graph()
    g.show()


if __name__ == '__main__':
    main()