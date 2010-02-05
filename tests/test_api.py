import re

from faker import Faker

f = Faker()

def test_instance():
    assert isinstance(f, Faker)

def test_fake_name():
    pattern = re.compile(r"(\w+\.? ?){2,3}")
    name = f.name()
    assert pattern.match(name)

def test_username():
    pattern = re.compile(r"^[a-z]*[^\s]$")
    username = f.username()
    assert pattern.match(username)

def test_fake_email():
    pattern = re.compile(r".+@.+\.\w+")
    email = f.email()
    assert pattern.match(email)

def test_lorem():
    pattern = re.compile(r"\w*")
    paragraph = f.lorem()
    assert pattern.match(paragraph)

def test_address():
    pattern = re.compile(r"""(\d+)\s+           # first numbers
                             (.*)?(?:\w\w)\s+   # street address
                             (\w\w)\s+          # state
                             (\d{5})\s+         # zip
                             (.*)               # the rest
                          """, re.X)
    address = f.address()
    assert pattern.match(address)

def test_phonenumber():
    pattern = re.compile(r"(\d{3}-\d{3}-\d{4})\s+")
    phonenumber = f.phonenumber()
    assert pattern.match(phonenumber)