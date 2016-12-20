import random


class User(object):
    def __init__(self, user_id, name):
        self.name = name
        self.user_id = user_id


class UserNotFoundError(Exception):
    def __init__(self, user_id, msg):
        super().__init__(msg)
        self.user_id = user_id


class SQLError(Exception):
    pass


class Repository:
    def __init__(self):
        self.fake_data = [
            User(1, 'Jeff'),
            User(2, 'Bill'),
            User(3, 'Ted'),
            User(4, 'Zoe')
        ]

    def find_user(self, user_id):

        e = random.randint(0, 2)
        if e == 1:
            raise SQLError

        for u in self.fake_data:
            if u.user_id == user_id:
                return u
        raise UserNotFoundError(user_id, 'Sorry user not found')

    def clean_up(self):
        print('Cleaning up the repository, bye now!')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.clean_up()

    def __enter__(self):
        return self


def find_user():
    with Repository() as r:
        user_id = input('Who do you want to find?')
        user = r.find_user(int(user_id))
        print('Cool you found {}'.format(user.name))


def main():
    try:
        find_user()

        #r = Repository()
        #user_id = input('Who do you want to find?')
        #user = r.find_user(int(user_id))
        #print('Cool you found {}'.format(user.name))
    #except:
        #print('sorry, we have a FAILURE!')
    except SQLError:
        print('Sorry the database is offline')
    except UserNotFoundError as unf:
        print('Sorry, user with id {} does not exist.'.format(unf.user_id))
    except ValueError:
        print('Oooooops we expected a number here!')
    except Exception as e:
        print('sorry, we have a this kind of failure: ' + str(e) + ' ' + str(type(e)))
    finally:
        print('Thanks for playing!')



if __name__ == '__main__':
    print('running')
    main()
