from python_accounting_app import data

def test_initial_balance():
    d = data.DataStore()
    assert d.read_balance() == 1000.00

def test_write_and_read_balance():
    d = data.DataStore()
    d.write_balance(1234.56)
    assert d.read_balance() == 1234.56
