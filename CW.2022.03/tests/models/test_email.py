import pytest
from models.email import Label, Email


@pytest.fixture(scope="function")
def sample():
    return Email(
        "sender@example.com",
        "recipient@example.com",
        "Test subject",
        "Test content",
        Label.Important,
    )


def test_add_label(capsys, sample):
    assert sample.labels == []
    assert sample.add_label(Label.Star) is True
    assert sample.labels == [Label.Star]
    assert sample.add_label(Label.Star) is False
    assert sample.labels == [Label.Star]

    with capsys.disabled():
        print(f"Tested {Email.add_label.__name__} successfully.")


def test_remove_label(capsys, sample):
    assert sample.labels == []
    assert sample.add_label(Label.Star) is True
    assert sample.remove_label(Label.Star) is True
    assert sample.labels == []
    assert sample.remove_label(Label.Star) is False
    assert sample.labels == []

    with capsys.disabled():
        print(f"Tested {Email.remove_label.__name__} successfully.")


def test_email_attributes(capsys, sample):
    assert sample.sender == "sender@example.com"
    assert sample.recipient == "recipient@example.com"
    assert sample.subject == "Test subject"
    assert sample.content == "Test content"
    assert sample.priority == Label.Important

    with capsys.disabled():
        print(f"Tested {sample.__class__.__name__} successfully.")
