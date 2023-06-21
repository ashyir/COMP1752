import pytest
from models.email import Label, Email


@pytest.fixture
def sample():
    return Email(
        "sender@example.com",
        "recipient@example.com",
        "Test subject",
        "Test content",
        Label.IMPORTANT,
    )


def test_add_label(sample):
    assert sample.labels == []
    assert sample.add_label(Label.STAR) is True
    assert sample.labels == [Label.STAR]
    assert sample.add_label(Label.STAR) is False
    assert sample.labels == [Label.STAR]


def test_remove_label(sample):
    assert sample.remove_label(Label.STAR) is True
    assert sample.labels == []
    assert sample.remove_label(Label.STAR) is False
    assert sample.labels == []


def test_email_attributes(sample):
    assert sample.sender == "sender@example.com"
    assert sample.recipient == "recipient@example.com"
    assert sample.subject == "Test subject"
    assert sample.content == "Test content"
    assert sample.priority == Label.IMPORTANT
