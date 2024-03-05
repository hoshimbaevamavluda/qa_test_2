import pytest


@pytest.fixture
def browser():
    print("Выполняется перед тестом")

    yield

    print("Выполняется тестом")


@pytest.fixture
def main_page(browser):
    pass


@pytest.fixture
def test_user():
    print("Тестовый пользователь")

    yield

    print("Здесь открываем")


def test_second(browser, test_user, main_page):
    pass
