import pytest

from src.concatenate import concatenate
from src.costs import get_total
from src.dictionary import Dictionary


def test_dictionary_stores_and_finds_entries():
    dictionary = Dictionary()

    dictionary.newentry("python", "programming language")

    assert dictionary.look("python") == "programming language"


def test_dictionary_returns_message_for_missing_entry():
    dictionary = Dictionary()

    assert dictionary.look("missing") == "cant find entry formissing"


def test_get_total_adds_known_items_and_tax():
    costs = {"apple": 1.0, "bread": 2.5, "milk": 3.0}
    items = ["apple", "milk", "unknown"]

    assert get_total(costs, items, 0.1) == 4.4


def test_concatenate_uses_matching_character_index():
    assert concatenate(["yoda", "best", "has"]) == "yes"


def test_concatenate_requires_list_input():
    with pytest.raises(TypeError):
        concatenate("not-a-list")
