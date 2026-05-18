from src.concatenate import concatenate

def test_basic():
    words = ["yoda", "best", "has"]
    assert concatenate(words) == "yes"

def test_example_pdf():
    words = ["apple", "banana", "cherry", "date"]
    assert concatenate(words) == "aaee"

def test_empty_list():
    assert concatenate([]) == ""

def test_non_string_items():
    words = ["hi", 123, None, "test"]
    assert concatenate(words) == "ht"