# demo_ci_cpython

Toy example of a Python CI pipeline inspired by CPython practices.

## Project idea

The package provides a small `Calculator` class with methods:
- `add`
- `sub`
- `mul`
- `div`

Tests are split by operation:
- `tests/test_add.py`
- `tests/test_sub.py`
- `tests/test_mul.py`
- `tests/test_div.py`

This structure makes CI failures easy to explain in demos.

## CI workflow design

- `ci.yml` orchestrates all checks.
- `lint.yml` runs lint checks.
- `mypy.yml` runs static type checks.
- `test.yml` is a reusable test workflow called from `ci.yml`.
- `ci.yml` runs tests through a matrix of operating systems:
  - `ubuntu-latest`
  - `windows-latest`
  - `macos-latest`

## Local verification

Run before pushing:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Run a specific test file:

```bash
pytest -q tests/test_div.py
```

<!-- ## Demo scenario: red/green pipeline

1. Start from a green branch where all checks pass.
2. Create a feature branch and introduce a bug in `Calculator.div` (for example, break zero-division behavior).
3. Open/update the PR and show that CI turns red (`test_div.py` fails).
4. Commit a fix that restores the `ZeroDivisionError` contract.
5. Show CI turning green again.

This demonstrates that the failure is caused by application logic regression, not CI infrastructure. -->
