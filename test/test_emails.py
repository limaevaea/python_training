import re


def test_emails_on_homepage(app):
    emails_from_homepage = app.contact.get_contact_list()[0] #[0] #проверка для первой записи
    emails_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert emails_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(emails_from_editpage)


def test_emails_on_contact_view_page(app):
    emails_from_view_page = app.contact.get_contact_from_view_page(0) #[0] #проверка для первой записи
    emails_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert emails_from_view_page.email == emails_from_editpage.email
    assert emails_from_view_page.email2 == emails_from_editpage.email2
    assert emails_from_view_page.email3 == emails_from_editpage.email3

def clear(s):
    return re.sub(r"[() -]", "", s)

def merge_emails_like_on_homepage(contact):
    return '\n'.join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))