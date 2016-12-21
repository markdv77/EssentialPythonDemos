class CartItem(object):
    def __init__(self, name, price):
        self.price = price
        self.name = name


class ShoppingCart(object):
    def __init__(self, customer_id):
        if customer_id <= 0:
            raise Exception('must be greater than 0')
        self.__customer_id = customer_id
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    @property
    def total_price(self):
        total = 0
        for item in self.__items:
            total += item.price
        return total

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, val):
        if val <= 0:
            raise Exception('must be greater than 0')

        val = int(val)

        self.__customer_id = val

    def __str__(self):
        return 'Cart with {0} items, total ${1:,}' \
            .format(len(self.__items), self.total_price)

    def __iter__(self):
        # return self.__items.__iter__()
        for item in self.__items:
            yield item


def main():
    cart = ShoppingCart(42)
    cart.hobbies = ['biking', 'skiing']

    print(cart.customer_id)
    cart.add(CartItem("CD", 19.00))
    cart.add(CartItem("Record", 17.50))

    for item in cart:
        print('{0} for ${1:,}'.format(item.name, item.price))

    print('Total is ${0:,}.'.format(cart.total_price))

    # print(cart)
    # print(cart.hobbies)

    # print(cart.__dict__)


if __name__ == '__main__':
    main()
