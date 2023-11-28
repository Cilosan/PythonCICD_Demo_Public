import python_app

def test_addition():
    assert python_app.add_numbers(3, 1) == 4
    assert python_app.add_numbers(8, -2) == 6
    assert python_app.add_numbers(0, -2) == -2

