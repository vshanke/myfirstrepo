from myapp.myfunc import add
import requests

def test_add():
    assert add(2,3) == 5

def test_add1():
    assert add(2,6) == 8

def test_add2():
    assert add(2,5) == 7

def test_add3():
    assert add(2, 2) == 4

# tests/test_jsonplaceholder.py

def test_get_post_1():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
