from python_accounting_app import operation, data

def test_operation_total_reads_balance():
    d = data.DataStore()
    op = operation.Operation(d)
    result = op.total()
    assert result == 1000.00  # solde initial

def test_operation_credit_updates_balance():
    d = data.DataStore()
    op = operation.Operation(d)
    op.credit(200.00)
    assert d.read_balance() == 1200.00

def test_operation_debit_updates_balance():
    d = data.DataStore()
    op = operation.Operation(d)
    op.debit(300.00)
    assert d.read_balance() == 700.00

def test_operation_debit_insufficient_funds():
    d = data.DataStore()
    op = operation.Operation(d)
    result = op.debit(2000.00)
    assert result == "Insufficient funds"
    assert d.read_balance() == 1000.00
