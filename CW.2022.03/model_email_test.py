import pytest
from model_email import Label, Email


@pytest.fixture
def sample_email():
    return Email(
        "sender@example.com",
        "recipient@example.com",
        "Test subject",
        "Test content",
        Label.Important,
    )


def test_add_label(sample_email):
    assert sample_email.labels == []
    assert sample_email.add_label(Label.Star) is True
    assert sample_email.labels == [Label.Star]
    assert sample_email.add_label(Label.Star) is False
    assert sample_email.labels == [Label.Star]


def test_remove_label(sample_email):
    assert sample_email.labels == []
    assert sample_email.add_label(Label.Star) is True
    assert sample_email.remove_label(Label.Star) is True
    assert sample_email.labels == []
    assert sample_email.remove_label(Label.Star) is False
    assert sample_email.labels == []


def test_email_attributes(sample_email):
    assert sample_email.sender == "sender@example.com"
    assert sample_email.recipient == "recipient@example.com"
    assert sample_email.subject == "Test subject"
    assert sample_email.content == "Test content"
    assert sample_email.priority == Label.Important
