from controller_account import AccountController
from model_account import Account, Gender


def test_account(capsys):
    account_controller = AccountController()
    account = Account(
        "test@test.com",
        "p@ssword",
        "Tester 01",
        "Tester",
        "01",
        "01/01/2000",
        Gender.Female,
    )

    # Test creating an account.
    assert account_controller.create_account(account) == True
    assert account_controller.accounts[account.email] == account

    assert account_controller.create_account(account) == False
    assert account_controller.accounts[account.email] == account

    # Test authenticating a user.
    assert account_controller.authenticate("test@test.com", "p@ssword") == True
    assert account_controller.authenticate("", "") == False
    assert account_controller.authenticate("", "p@ssword") == False
    assert account_controller.authenticate("test@test.com", "") == False
    assert account_controller.authenticate("a@test.com", "p@ssword") == False
    assert account_controller.authenticate("test@test.com", "a") == False
    assert account_controller.authenticate("a@test.com", "a") == False

    with capsys.disabled():
        print("Test model Account successfully.")
