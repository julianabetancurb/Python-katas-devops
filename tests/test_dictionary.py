import pytest
from src.dictionary import Dictionary

@pytest.fixture
def sample_dict():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")
    return d

def test_existing_word(sample_dict):
    assert sample_dict.look("Apple") == "A fruit that grows on trees"

def test_missing_word(sample_dict):
    assert sample_dict.look("Banana") == "Can't find entry for Banana"