from src.costs import get_total

def test_total_with_tax():
    costs = {"socks": 5, "shoes": 60, "sweater": 30}
    items = ["socks", "shoes"]
    tax = 0.09
    assert get_total(costs, items, tax) == 70.85

def test_ignore_unknown_items():
    costs = {"socks": 5}
    items = ["socks", "hat"]
    tax = 0.10
    assert get_total(costs, items, tax) == 5.50

def test_empty_cart():
    costs = {"socks": 5}
    items = []
    tax = 0.1
    assert get_total(costs, items, tax) == 0.0