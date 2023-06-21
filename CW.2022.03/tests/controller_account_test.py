import pytest

from controllers.account import AccountController
from models.account import Account, Gender


@pytest.fixture
def sample():
    return Account(
        "test@test.com",
        "p@ssword",
        "Tester 01",
        "Tester",
        "01",
        "01/01/2000",
        Gender.FEMALE,
    )


def test_create_account(sample):
    account_controller = AccountController()

    assert len(account_controller.accounts) == 0
    assert account_controller.create_account(sample) == True
    assert account_controller.accounts[sample.email] == sample
    assert len(account_controller.accounts) == 1

    assert account_controller.create_account(sample) == False
    assert account_controller.accounts[sample.email] == sample
    assert len(account_controller.accounts) == 1


def test_authenticate(sample):
    account_controller = AccountController()

    assert account_controller.authenticate(sample.email, sample.password) == True
    assert account_controller.authenticate("", "") == False
    assert account_controller.authenticate("", sample.password) == False
    assert account_controller.authenticate(sample.email, "") == False
    assert account_controller.authenticate("wrong@test.com", sample.password) == False
    assert account_controller.authenticate(sample.email, "wrong") == False
    assert account_controller.authenticate("wrong@test.com", "wrong") == False


# Add more unit tests here.
