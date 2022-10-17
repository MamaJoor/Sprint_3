import random


def gen_email():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = random.randint(6, 10)
    email = ''
    for i in range(length):
        email += random.choice(chars)
    email = str(email) + "@ya.ru"
    # print(email)
    return email


def gen_password():
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    length = random.randint(6, 10)
    password = ''
    for i in range(length):
        password += random.choice(chars)
    # print(password)
    return password
