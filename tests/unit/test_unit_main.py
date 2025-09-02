import builtins
import pytest
from unittest.mock import patch, MagicMock
from python_accounting_app import main

def test_choice_1_calls_total(monkeypatch):
    mock_ops = MagicMock()
    monkeypatch.setattr(main, "call_operations", mock_ops)
    main.handle_choice("1")
    mock_ops.assert_called_once_with("TOTAL")

def test_choice_2_calls_credit(monkeypatch):
    mock_ops = MagicMock()
    monkeypatch.setattr(main, "call_operations", mock_ops)
    main.handle_choice("2")
    mock_ops.assert_called_once_with("CREDIT")

def test_choice_3_calls_debit(monkeypatch):
    mock_ops = MagicMock()
    monkeypatch.setattr(main, "call_operations", mock_ops)
    main.handle_choice("3")
    mock_ops.assert_called_once_with("DEBIT")

def test_choice_4_exits(monkeypatch):
    assert main.handle_choice("4") == "EXIT"

def test_invalid_choice(monkeypatch, capsys):
    result = main.handle_choice("9")
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
    assert result is None

def test_non_numeric_choice(monkeypatch, capsys):
    result = main.handle_choice("abc")
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out
    assert result is None

def test_menu_loop_exit(monkeypatch):
    # Simule une séquence d'inputs : 1, 2, 4 (sortie)
    inputs = iter(["1", "2", "4"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    with patch.object(main, "call_operations") as mock_ops:
        main.menu_loop()
        assert mock_ops.call_count == 2  # 1 et 2
