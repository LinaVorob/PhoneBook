class UnknownUser(Exception):
    def __str__(self):
        return 'Unknown user. Complete the registration.'

class WrongPassword(Exception):
    def __str__(self):
        return 'Wrong password. Try again'