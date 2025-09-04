from unittest.mock import MagicMock
from python_accounting_app import operation

def test_credit_valid_amount():
    mock_data = MagicMock()
    mock_data.read_balance.return_value = 1000.00
    op = operation.Operation(mock_data)
    op.credit(100.00)
    mock_data.write_balance.assert_called_with(1100.00)

def test_credit_zero_amount():
    mock_data = MagicMock()
    mock_data.read_balance.return_value = 1000.00
    op = operation.Operation(mock_data)
    op.credit(0.00)
    mock_data.write_balance.assert_called_with(1000.00)

def test_debit_valid_amount():
    mock_data = MagicMock()
    mock_data.read_balance.return_value = 1000.00
    op = operation.Operation(mock_data)
    op.debit(200.00)
    mock_data.write_balance.assert_called_with(800.00)

def test_debit_insufficient_funds():
    mock_data = MagicMock()
    mock_data.read_balance.return_value = 1000.00
    op = operation.Operation(mock_data)
    result = op.debit(2000.00)
    assert result == "Insufficient funds"
    mock_data.write_balance.assert_not_called()

def test_debit_zero_amount():
    mock_data = MagicMock()
    mock_data.read_balance.return_value = 1000.00
    op = operation.Operation(mock_data)
    op.debit(0.00)
    mock_data.write_balance.assert_called_with(1000.00)
