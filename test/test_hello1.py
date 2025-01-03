from test.hello1 import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Edward") == "hello, Edward"

