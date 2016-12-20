class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('The animal is running...')


class Zebra(Animal):
    def __init__(self, name, stripiness):
        super().__init__(name)
        self.stripiness = stripiness

    def run(self):
        super().run()
        print('The zebra known as {} gallops with stripe factor of {}!'\
              .format(self.name, self.stripiness))


def main():
    zebra = Zebra('jeff', 11)
    zebra.run()


if __name__ == '__main__':
    main()
