import string
import random


def get_new_id():
    newId = ''.join(random.choice(string.ascii_lowercase \
        + string.digits) for i in range(20))
    return newId
