# Progress Log

Started: 2026-10-10. Background: Oracle SQL/PL/SQL. Goal: data + AI (Python, pandas, Oracle, LLMs).

## Topics covered

| # | Topic | Script | Status |
|---|---|---|---|
| 1 | Variables, if/else, loops, functions | `01_functions_dicts.py` | Solid |
| 2 | return vs print | `01_functions_dicts.py` | Solid |
| 3 | Dict loops (`.items()`), comprehension | `01_functions_dicts.py` | OK, re-practice reading comprehensions |
| 4 | Lists, indexing, negative index, slicing | `02_lists_tuples_sets.py` | OK, slicing with negatives needs practice |
| 5 | Tuples, unpacking | `02_lists_tuples_sets.py` | OK |
| 6 | Sets, set vs dict | `02_lists_tuples_sets.py` | OK |
| 7 | Reading a file | `03_read_file.py` | Solid |
| 8 | Comparison operators | `03_read_file.py` | OK |
| 9 | try / except / finally | `04_error_handling.py` | OK |
| 10 | TypeError vs ValueError, str/int conversion | `04_error_handling.py` | OK |
| 11 | f-strings | `05_read_write_file.py` | Just started |
| 12 | Writing a file | `05_read_write_file.py` | Shaky, needs more practice |

## Bug log (my mistakes and the lesson)

| # | Bug | Error / effect | Fix and lesson |
|---|---|---|---|
| 1 | Curly quotes `" "` from phone keyboard | `SyntaxError` | Use straight `" "`. Write code in VS Code, not on the phone |
| 2 | `Def`, `For`, `If`, `Print`, `Return` capitalised | `SyntaxError` / `NameError` | Python is case-sensitive. Keywords are lowercase |
| 3 | Missing `:` after `def`, `for`, `if`, `with` | `SyntaxError` | Every block header ends with a colon. Not after `.split(",")` |
| 4 | Looped a dict and compared the key to a number | `TypeError` | Looping a dict gives keys. Use `.items()` for key and value |
| 5 | Used `emp` inside a function whose parameter is `emps` | `NameError` | Use the parameter name inside the function |
| 6 | `return` inside the loop | Stops after first match | Put `return` after the loop |
| 7 | Name mismatch: `nam` vs `n`, `lines` vs `line` | `NameError` | Use one name everywhere |
| 8 | `open(emps.txt)` | `NameError` | File name is text: `open("emps.txt") as f` |
| 9 | Wrong indentation (`for` outside `with`, `if` outside `for`) | `NameError` or wrong result | Indentation is the block structure, like `END IF` |
| 10 | Thought `names[2]` was null | Wrong answer | Index 2 is the third item. Python has `None`, and out of range is `IndexError` |
| 11 | Mixed up `names` and `salaries` in an index question | Wrong answer | The list name decides the value |
| 12 | `names[-2:]` answered `Ann, Manoj` | Wrong answer | Slices keep original order: `['Ann', 'Raj']` |
| 13 | `min_max([7,3,10,1])` answered `(3,10)` | Wrong answer | `min` scans the whole list: `(1, 10)` |
| 14 | `len({5,5,6,7,7})` answered 5 | Wrong answer | Set drops duplicates first: 3 |
| 15 | Used `=` to compare | `SyntaxError` | `=` assigns, `==` compares |
| 16 | Wrong filter result for `> 30000` (missed Manoj) | Wrong answer | Check every row against the condition |
| 17 | `except TypeError` for an `int("abc")` error | Crash, not caught | Name after `except` must match the raised error (`ValueError`) |
| 18 | Fix direction for `"Total: " + 500` | Wrong fix | Joining text: `str(500)`. Calculating: `int("29000")` |
| 19 | `/n` instead of `\n`, with a space before it | Literal `/n` in file | Newline is backslash-n, right after the data |
| 20 | `write()` with no `\n` | `Ann,29000Lee,41000` on one line | `write()` does not add a newline, `print()` does |
| 21 | Opened `high.txt` with `"w"` inside the loop | File erased each row | Open output once, outside the loop |
| 22 | `as out.write` and `out.write(nam, sal)` | `SyntaxError` / `TypeError` | `as out`, then `out.write(f"{name},{sal}\n")` |
| 23 | Unneeded `result = {}` when writing straight to a file | Extra code | Only build a container if you need to return or reuse it |

## Patterns that keep repeating

1. Most errors are typos (quotes, colons, case, names), not logic. Read the code once, top to bottom, before running.
2. Text vs number: file data is always text. Convert with `int()` before comparing or calculating.
3. Check which list or variable the question asks about before answering.

## Next steps

- [ ] Run all five scripts in VS Code and compare with the comments
- [ ] Rewrite `05_read_write_file.py` from memory, without looking
- [ ] Practice writing files until it feels natural (e.g. save the below-30000 rows to `low.txt`)
- [ ] CSV with the `csv` module
- [ ] Libraries and `pip`, then `pandas`
- [ ] Connect Python to Oracle
- [ ] First LLM API call

## Git workflow

```bash
git init
git add .
git commit -m "Add practice scripts and progress log"
```

After each practice session: update the log (new topics, new bugs), then

```bash
git add .
git commit -m "Practice: <topic>"
```
