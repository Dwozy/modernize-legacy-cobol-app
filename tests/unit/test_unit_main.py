import builtins
import pytest
from unittest.mock import patch, MagicMock
from python_accounting_app import main

def test_choice_1_calls_total(monkeypatch):
    mock_ops = MagicMock()
    monkeypatch.setattr(main, "call_operations", mock_ops)
    main.handle_choice("1", mock_ops)
    main.call_operations.assert_called_once_with("TOTAL", mock_ops)

def test_choice_2_calls_credit(monkeypatch):
    mock_ops = MagicMock()
    monkeypatch.setattr(main, "call_operations", mock_ops)
    main.handle_choice("2", mock_ops)
    main.call_operations.assert_called_once_with("CREDIT", mock_ops)

def test_choice_3_calls_debit(monkeypatch):
    mock_ops = MagicMock()
    monkeypatch.setattr(main, "call_operations", mock_ops)
    main.handle_choice("3", mock_ops)
    main.call_operations.assert_called_once_with("DEBIT", mock_ops)

def test_choice_4_exits():
    mock_ops = MagicMock()
    assert main.handle_choice("4", mock_ops) == "EXIT"

def test_invalid_choice(capsys):
    mock_ops = MagicMock()
    result = main.handle_choice("9", mock_ops)
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
    assert result is None

def test_non_numeric_choice(capsys):
    mock_ops = MagicMock()
    result = main.handle_choice("abc", mock_ops)
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
    assert result is None

def test_menu_loop_exit(monkeypatch):
    inputs = iter(["1", "2", "4"])
    monkeypatch.setattr(builtins, "input", lambda: next(inputs))
    mock_ops = MagicMock()
    with patch.object(main, "call_operations") as mock_call_ops:
        main.menu_loop(mock_ops)
        assert mock_call_ops.call_count == 2

@pytest.mark.parametrize(
    "inputs,expected",
    [
        (["123,45"], 123.45),      # virgule
        (["678.90"], 678.90),      # point
        (["0"], 0.0),              # zéro accepté
        (["42"], 42.0),            # entier positif
        (["0.01"], 0.01),          # petit décimal
    ]
)
def test_get_valid_amount_valid_cases(monkeypatch, inputs, expected):
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda *args: next(it))
    result = main.get_valid_amount("Enter amount:")
    assert result == expected

@pytest.mark.parametrize(
    "inputs,expected,invalid_count",
    [
        (["abc", "123,45"], 123.45, 1),           # texte puis valide
        (["", "notanumber", "678.90"], 678.90, 2),# vide, texte, puis valide
        (["-123,45", "42"], 42.0, 1),             # négatif refusé, puis positif accepté
        ([" ", "0"], 0.0, 1),                     # espace, puis zéro accepté
        (["10.35.65", "123,45"], 123.45, 1),      # format non float, puis valide
    ]
)
def test_get_valid_amount_invalid_cases(monkeypatch, capsys, inputs, expected, invalid_count):
    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda *args: next(it))
    result = main.get_valid_amount("Enter amount:")
    assert result == expected
    output = capsys.readouterr().out
    assert output.count("Invalid amount") == invalid_count

def test_credit_caps_balance_and_warns(monkeypatch, capsys):
    # Simule un solde proche du plafond et un crédit trop grand
    class MockOps:
        def total(self):
            return 999980.00
        def credit(self, amount):
            return 999999.99
    mock_ops = MockOps()
    monkeypatch.setattr(builtins, "input", lambda *args: "10000")
    main.call_operations("CREDIT", mock_ops)
    output = capsys.readouterr().out
    assert "Warning: Maximum balance is 999999.99. The balance has been capped at this limit." in output
    assert "Amount credited. New balance: 999999.99" in output
