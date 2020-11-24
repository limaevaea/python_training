

def test_firstnames_on_homepage(app):
    names_from_homepage = app.contact.get_contact_list()[0] #[0] #проверка для первой записи
    names_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert names_from_homepage.firstname == names_from_editpage.firstname


def test_lastnames_on_homepage(app):
    names_from_homepage = app.contact.get_contact_list()[0] #[0] #проверка для первой записи
    names_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert names_from_homepage.lastname == names_from_editpage.lastname




