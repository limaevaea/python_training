
def test_address_on_homepage(app):
    address_from_homepage = app.contact.get_contact_list()[0] #[0] #проверка для первой записи
    address_from_editpage = app.contact.get_contact_info_from_edit_page(0) #со страницы редактиро
    assert address_from_homepage.address == address_from_editpage.address