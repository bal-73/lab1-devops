# Lab 1: Python CI Pipeline with GitHub Actions

This repository demonstrates a simple Python project with automated testing using GitHub Actions.

## Project Overview
- Contains a Python function `add(a, b)` in `app.py`.
- Contains test cases for the function in `test_app.py` using `pytest`.
- GitHub Actions workflow automatically runs tests whenever code is pushed to the `main` branch.

## Files
- `app.py` → Python function `add(a, b)`  
- `test_app.py` → Test cases for the `add` function  
- `.github/workflows/python-ci.yml` → GitHub Actions workflow file  
- `README.md` → Project documentation

## How to Run Locally
1. Make sure Python 3.10 (or above) is installed.  
2. Install pytest (if not installed):  
```bash
pip install pytest

3.Run the script:
bash
python app.py

4.Run tests:
bash
pytest

GitHub Actions
The workflow runs automatically on every push to the main branch.

If all tests pass, the workflow shows a ✅ green check.

If any test fails, the workflow shows a ❌ red cross, and you can check the logs for details.

Author
Ahmad Iqbal
