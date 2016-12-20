class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies


def main(people):
    people = [
        Person('Jeff', 42, ['tennis', 'hockey', 'football']),
        Person('Michael', 40, ['biking', 'hiking', 'motocross']),
        Person('Pierce', 39, ['biking', 'kite boarding']),
        Person('Stacey', 32, ['skiing'])
    ]

    # Question: who is a biker?
    bikers = [
        p.name.upper()  # select
        for p in people  # datasource
        if 'biking' in p.hobbies  # filter
        ]

    bikers_gen = (
        p.name.upper()  # select
        for p in people  # datasource
        if 'biking' in p.hobbies  # filter
    )

    print(type(bikers))
    print(type(bikers_gen))

    print('list comprehension output:')
    for biker in bikers:
        print(biker)

    print('generator expression output:')
    for biker in bikers_gen:
        print(biker)


if __name__ == '__main__':
    main()
