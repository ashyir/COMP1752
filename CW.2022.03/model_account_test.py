from model_account import Account, Gender

def test_model_account(capsys):
    account = Account("test@test.com", "p@ssword", "Tester 01", "Tester", "01", "01/01/2000", Gender.Female)

    assert account.email == "test@test.com"
    assert account.password == "p@ssword"
    assert account.display_name == "Tester 01"
    assert account.first_name == "Tester"
    assert account.last_name == "01"
    assert account.birthday == "01/01/2000"
    assert account.gender == Gender.Female

    with capsys.disabled():
        print("Test model Account successfully.")