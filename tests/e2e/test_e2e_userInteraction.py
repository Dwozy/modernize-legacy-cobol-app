import builtins
from python_accounting_app import main

def test_full_user_journey(monkeypatch, capsys):
    # Simule : voir, créditer, débiter, quitter
    inputs = iter([
        "1",      # View balance
        "2",      # Credit
        "100.00", # Credit amount
        "3",      # Debit
        "50.00",  # Debit amount
        "4"       # Exit
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    main.run()
    output = capsys.readouterr().out
    assert "Current balance: 1000.00" in output
    assert "Amount credited. New balance: 1100.00" in output
    assert "Amount debited. New balance: 1050.00" in output
    assert "Exiting the program. Goodbye!" in output

def test_debit_insufficient(monkeypatch, capsys):
    inputs = iter([
        "3",      # Debit
        "2000.00",# Debit amount
        "4"       # Exit
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    main.run()
    output = capsys.readouterr().out
    assert "Insufficient funds" in output
