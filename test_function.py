from myfunc import add

def test_add():
    assert add(2,3) == 5

def test_add1():
    assert add(2,6) == 8

def test_add2():
    assert add(2,5) == 7

def test_add3():
    assert add(2, 2) == 4
