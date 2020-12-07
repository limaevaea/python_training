from model.сontact import Сontact
import random #выбираем случано
import string #содержит константы списки символов


testdata = [
    Сontact(firstname="Ivanova", middlename="Ekaterina", lastname="last1"),
    Сontact(firstname="Petrova", middlename="Ekaterina", lastname="last2")
]

'''constant = [
    Сontact(firstname="Ivanova", middlename="Ekaterina", lastname="last1"),
    Сontact(firstname="Petrova", middlename="Ekaterina", lastname="last2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Сontact(firstname="", middlename="Ekaterina", lastname="")] + [
    Сontact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("lastname", 10), title="w",
            company="company123", address="Moscow mirovaya 1-23", home="8-912-854-854", mobile="12345", work="2345", email="testirovanie@mail.comcom",
            birth_date="16", birth_month="January", birth_year="1988")
    for i in range(5)
]'''