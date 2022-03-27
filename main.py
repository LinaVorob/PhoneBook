from database import PhoneDB


class PhoneBook:
    def __init__(self):
        self.db = PhoneDB()


if __name__ == '__main__':
    app = PhoneBook()
