def get_total(costs, items, tax):
    total = 0
    for item in items:
        if item in costs:
            total += costs[item]
    return round(total * (1 + tax), 2)