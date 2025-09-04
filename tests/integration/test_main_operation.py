from python_accounting_app import main, operation
from unittest.mock import MagicMock

def test_main_calls_operation_total(monkeypatch):
    called = {}
    def fake_total(self):
        called['total'] = True
        return 0
    monkeypatch.setattr(operation.Operation, "total", fake_total)
    mock_data_store = MagicMock()
    ops = operation.Operation(mock_data_store)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    main.handle_choice("1", ops)
    assert called.get('total') is True

def test_main_calls_operation_credit(monkeypatch):
    called = {}
    def fake_credit(self, amount):
        called['credit'] = True
        return 0
    monkeypatch.setattr(operation.Operation, "credit", fake_credit)
    mock_data_store = MagicMock()
    mock_data_store.read_balance.return_value = 1000.00  # <-- Fix here
    ops = operation.Operation(mock_data_store)
    monkeypatch.setattr("builtins.input", lambda: "1")
    main.handle_choice("2", ops)
    assert called.get('credit') is True

def test_main_calls_operation_debit(monkeypatch):
    called = {}
    def fake_debit(self, amount):
        called['debit'] = True
        return 0
    monkeypatch.setattr(operation.Operation, "debit", fake_debit)
    mock_data_store = MagicMock()
    ops = operation.Operation(mock_data_store)
    monkeypatch.setattr("builtins.input", lambda: "1")
    main.handle_choice("3", ops)
    assert called.get('debit') is True
