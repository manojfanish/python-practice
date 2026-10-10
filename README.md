# Python Practice

My Python learning log, coming from an Oracle SQL/PL/SQL background.
Goal: data + AI skills (Python, then pandas, Oracle connectivity, LLMs).

## Structure

| File | Topic |
|---|---|
| `01_functions_dicts.py` | functions, return vs print, dict loops, comprehension |
| `02_lists_tuples_sets.py` | indexing, slicing, tuples, sets |
| `03_read_file.py` | reading `emps.txt`, split, `int()` |
| `04_error_handling.py` | try / except / finally |
| `05_read_write_file.py` | read `emps.txt`, write `high.txt` |
| `emps.txt` | sample data |
| `PROGRESS_LOG.md` | topics covered + my bugs and lessons |

## How to run

```bash
python 01_functions_dicts.py
```

Run from the repo folder so `emps.txt` is found.

## PL/SQL cheat sheet

| Python | PL/SQL |
|---|---|
| `print()` | `DBMS_OUTPUT.PUT_LINE` |
| `return` | `RETURN` |
| `int()` / `str()` | `TO_NUMBER()` / `TO_CHAR()` |
| `try / except` | `BEGIN ... EXCEPTION ... END` |
| `ValueError` | `INVALID_NUMBER` |
| `=` / `==` | `:=` / `=` |
| `!=` | `<>` |
| `open(..., "w")` | `UTL_FILE.FOPEN(..., 'W')` |
