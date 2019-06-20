import pytest


@pytest.mark.parametrize(
    'qty_poured, query_row, query_glass, expected_qty', [
        (0, 0, 0, 0),
        (0.25, 0, 0, 0.2500),
        (0.30, 0, 0, 0.2500),
    ]
)
def test_calculate_quantity_at_row_0(qty_poured, query_row, query_glass, expected_qty, flow):
    qty = flow.calculate_quantity(qty_poured, query_row, query_glass)
    assert qty == expected_qty


@pytest.mark.parametrize(
    'qty_poured, query_row, query_glass, expected_qty', [
        (0.25, 1, 0, 0),
        (0.25, 1, 1, 0),
        (0.30, 1, 0, 0.0250),
        (0.30, 1, 1, 0.0250),
        (0.75, 1, 0, 0.2500),
        (0.75, 1, 1, 0.2500),
        (0.80, 1, 0, 0.2500),
        (0.80, 1, 1, 0.2500),
    ]
)
def test_calculate_quantity_at_row_1(qty_poured, query_row, query_glass, expected_qty, flow):
    qty = flow.calculate_quantity(qty_poured, query_row, query_glass)
    assert qty == expected_qty


@pytest.mark.parametrize(
    'qty_poured, query_row, query_glass, expected_qty', [
        (0.75, 2, 0, 0),
        (0.75, 2, 1, 0),
        (0.75, 2, 2, 0),
        (1, 2, 0, 0.0625),
        (1, 2, 1, 0.1250),
        (1, 2, 2, 0.0625),
        (2, 2, 0, 0.2500),
        (2, 2, 1, 0.2500),
        (2, 2, 2, 0.2500),
    ]
)
def test_calculate_quantity_at_row_2(qty_poured, query_row, query_glass, expected_qty, flow):
    qty = flow.calculate_quantity(qty_poured, query_row, query_glass)
    assert qty == expected_qty


@pytest.mark.parametrize(
    'qty_poured, query_row, query_glass, expected_qty', [
        (1, 3, 0, 0),
        (1, 3, 1, 0),
        (1, 3, 2, 0),
        (1, 3, 3, 0),
        (2, 3, 0, 0.0312),
        (2, 3, 1, 0.2188),
        (2, 3, 2, 0.2188),
        (2, 3, 3, 0.0312),
        (5, 3, 0, 0.2500),
        (5, 3, 1, 0.2500),
        (5, 3, 2, 0.2500),
        (5, 3, 3, 0.2500),
    ]
)
def test_calculate_quantity_at_row_3(qty_poured, query_row, query_glass, expected_qty, flow):
    qty = flow.calculate_quantity(qty_poured, query_row, query_glass)
    assert qty == expected_qty
