from model.сontact import Сontact
import random #выбираем случано
import string #содержит константы списки символов
import os.path
import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Сontact(firstname="", middlename="Ekaterina", lastname="")] + [
    Сontact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("lastname", 10), title="w",
            company="company123", address="Moscow mirovaya 1-23", home="8-912-854-854", mobile="12345", work="2345", email="testirovanie@mail.comcom",
            birth_date="16", birth_month="January", birth_year="1988")
    for i in range(n)
]

#save data in file
file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)

with open(file, "w") as rjson:
    jsonpickle.set_encoder_options("json", indent=2)
    rjson.write(jsonpickle.encode(testdata))