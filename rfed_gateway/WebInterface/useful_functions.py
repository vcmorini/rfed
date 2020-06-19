import random
import uuid
import json


def random_n_digits(n):
    result = ""
    for i in range(n):
        result += str(random.randint(0, 9))
    return result


def generate_mac():
    return "%02x%02x%02x%02x%02x%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )


def generate_unique_id():
    # We will create a database called IDs that is a hashmap between a simple idendifier generated by name surname and
    # date of birth of the patient and a more complex indentifier provided by this function.
    # Even if someone has access to this database, he will never directly see sensitive information but just 2 letters
    # with a secret combination of the date of birth.
    return str(uuid.uuid4())


def find_in_list(list, key, item):
    active_pos = None
    for i in range(len(list)):
        if list[i][key] == item[key]:
            active_pos = i
    return active_pos
