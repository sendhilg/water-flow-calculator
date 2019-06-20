from collections import deque
from unittest.mock import patch

from water_flow.command import Command


def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.popleft()
    return next_input


def test_command_parse_for_valid_input(capsys, monkeypatch):
    monkeypatch.setitem(
        __builtins__,
        'input',
        make_multiple_inputs(deque(['1.5', '2', '1']))
    )
    command = Command()
    command.parse()
    out, _ = capsys.readouterr()
    assert out == '\nAmount of water in glass number 1 of row number 2 is:\n0.25\n'


def test_command_parse_for_invalid_input(capsys, monkeypatch):
    monkeypatch.setitem(
        __builtins__,
        'input',
        make_multiple_inputs(deque(['1', '2', '3']))
    )
    command = Command()
    command.parse()
    out, _ = capsys.readouterr()
    assert out == '\nError: Glass number cannot be greater than row number.\n'


def test_command_parse_for_invalid_input_types(capsys, monkeypatch):
    monkeypatch.setitem(
        __builtins__,
        'input',
        make_multiple_inputs(deque(['A', '2', '3']))
    )
    command = Command()
    command.parse()
    out, _ = capsys.readouterr()
    assert out == '\nError: Enter numeric values for qty, row number, glass number.\n'


@patch('water_flow.flow.Flow.calculate_quantity', autospec=True)
def test_command_parse_calls_for_valid_input(mock_calculate_quantity, monkeypatch):
    monkeypatch.setitem(
        __builtins__,
        'input',
        make_multiple_inputs(deque(['1', '2', '1']))
    )

    command = Command()
    command.parse()

    mock_calculate_quantity.assert_called_once_with(command.flow, 1, 2, 1)


@patch('water_flow.flow.Flow.calculate_quantity', autospec=True)
def test_command_parse_calls_for_invalid_input(mock_calculate_quantity, monkeypatch):
    monkeypatch.setitem(
        __builtins__,
        'input',
        make_multiple_inputs(deque(['A', '2', '1']))
    )

    command = Command()
    command.parse()

    mock_calculate_quantity.assert_not_called()
