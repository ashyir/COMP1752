import pytest
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


def test_account_attribute(capsys, sample):
    assert sample.email == "test@test.com"
    assert sample.password == "p@ssword"
    assert sample.display_name == "Tester 01"
    assert sample.first_name == "Tester"
    assert sample.last_name == "01"
    assert sample.birthday == "01/01/2000"
    assert sample.gender == Gender.FEMALE
