from model_email import Email, Label

def test_model_email(capsys):
    email = Email("sender@test.com", "recipient@test.com", "Test Subject", "Test Content", 1)

    # Test initializing email.
    assert email.sender == "sender@test.com"
    assert email.recipient == "recipient@test.com"
    assert email.subject == "Test Subject"
    assert email.content == "Test Content"
    assert email.priority == 1
    assert len(email.labels) == 0

    # Test adding a label.
    assert email.add_label(Label.Important) == True
    assert email.add_label(Label.Important) == False
    assert len(email.labels) == 1
    assert email.labels[0] == Label.Important

    # Test removing a label.
    assert email.remove_label(Label.Star) == False
    assert email.remove_label(Label.Important) == True
    assert len(email.labels) == 0

    with capsys.disabled():
        print()
        print(f"Tested {email.__class__.__name__} successfully.")