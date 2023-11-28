from python_app import add_numbers

def test_addition():
    assert add_numbers(3, 1) == 4
    assert add_numbers(8, -2) == 6
    assert add_numbers(0, -2) == -2

