import pytest

from water_overflow.command import Command


@pytest.mark.parametrize(
    'qty_poured, query_row, query_glass, expected_qty', [
        (0, 0, 0, 0),
        (0.9, 0, 0, 0.9),
        (1, 0, 0, 1),
        (1.5, 0, 0, 1),
        (1.5, 1, 0, 0.25),
        (1.5, 1, 1, 0.25),
        (2, 1, 0, 0.5),
        (2, 1, 1, 0.5),
        (2.5, 1, 0, 0.75),
        (2.5, 1, 1, 0.75),
        (3, 1, 0, 1),
        (3, 1, 1, 1),
        (3.5, 1, 0, 1),
        (3.5, 1, 1, 1),
        (3.5, 2, 0, 0.125),
        (3.5, 2, 1, 0.25),
        (3.5, 2, 2, 0.125),
        (4, 2, 0, 0.25),
        (4, 2, 1, 0.50),
        (4, 2, 2, 0.25),
        (6, 2, 0, 0.75),
        (6, 2, 1, 1),
        (6, 2, 2, 0.75),
        (6, 3, 0, 0),
        (6, 3, 1, 0.25),
        (6, 3, 2, 0.25),
        # (6, 3, 3, 0),
        # (6, 3, 0, 0),
        # (6, 3, 1, 0),
        # (6, 3, 2, 0),
        # (6, 3, 3, 0),
    ]
)
def test_find_water_qty(qty_poured, query_row, query_glass, expected_qty):
    command = Command()
    qty = command.find_water_qty(qty_poured, query_row, query_glass)
    assert qty == expected_qty
