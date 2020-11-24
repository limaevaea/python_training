import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0] #[0] #проверка для первой записи
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_editpage)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0) #[0] #проверка для первой записи
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert contact_from_view_page.home == contact_from_editpage.home
    assert contact_from_view_page.mobile == contact_from_editpage.mobile
    assert contact_from_view_page.work == contact_from_editpage.work

def clear(s):
    return re.sub(r"[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda  x: clear(x),
                                filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work]))))