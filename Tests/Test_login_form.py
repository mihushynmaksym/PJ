import pytest
from application import Application

__author__ = 'Max'


@pytest.fixture(scope="session", autouse=True)# run all tests in one session.
def app(request):
    global fixture
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# ID = 1
def test_with_valid_login_and_password(app):
    print("\nID = 1")
    app.go_to_main_page()
    app.find_form_autotification()
    app.fill_login_form(login='tomsmith', password='SuperSecretPassword!')
    app.find_submit_button()
    app.make_screenshot(path='C:/screen/ID1.png')
