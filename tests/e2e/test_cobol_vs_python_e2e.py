import subprocess
import sys
import pytest
import os

def run_app(cmd, inputs):
    """Run an interactive CLI app and return its output as a string."""
    env = os.environ.copy()
    env.pop('COV_CORE_SOURCE', None)
    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env
    )
    input_str = "\n".join(inputs) + "\n"
    try:
        out, _ = proc.communicate(input=input_str, timeout=10)
    except subprocess.TimeoutExpired:
        proc.kill()
        out, _ = proc.communicate()
    return out

def test_cobol_vs_python_e2e():
    inputs = [
        "1",        # View balance
        "2", "100", # Credit 100
        "3", "50",  # Debit 50
        "3", "2000",# Debit too much
        "4"         # Exit
    ]

    cobol_cmd = ["./accountsystem"]
    python_cmd = [sys.executable, "-m", "python_accounting_app.main"]

    cobol_output = run_app(cobol_cmd, inputs)
    python_output = run_app(python_cmd, inputs)

    def normalize(s):
        return [line.strip() for line in s.splitlines() if line.strip()]

    cobol_lines = normalize(cobol_output)
    python_lines = normalize(python_output)

    if cobol_lines != python_lines:
        print("COBOL output:")
        print("\n".join(cobol_lines))
        print("PYTHON output:")
        print("\n".join(python_lines))

    assert cobol_lines == python_lines
