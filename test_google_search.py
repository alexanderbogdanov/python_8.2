from selene import browser
from selene import be, have


def test_google_search():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))


def test_google_search_negative():
    browser.element('[name="q"]').should(be.blank).type('234234243alalaдло').press_enter()
    browser.element('#botstuff').should(have.text('Your search - 234234243alalaдло - did not match any documents.'))
