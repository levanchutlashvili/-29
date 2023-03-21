from bank import value

def test_value_hello():
    assert value("hello world! ") == 0
    assert value("hi there! ") == 20
    assert value("good morning! ") == 100
    