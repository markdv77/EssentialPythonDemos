from db import DBORM


def main():
    db = DBORM()
    db.add_some_data()
    db.show_data()


if __name__ == '__main__':
    main()