

class contact:
    #делаем конструктор
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, home=None,
                 email=None, birth_date=None, birth_month=None, birth_year=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.email = email
        self.birth_date = birth_date
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.id = id