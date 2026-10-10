"""Topic 1: functions, return vs print, dict loops, comprehension."""

emps = {"Manoj": 50000, "Ann": 29000}


# Style 1: empty container + loop (like a PL/SQL collection you EXTEND)
def high_earners(emps):
    result = {}                      # empty box, filled inside the loop
    for name, sal in emps.items():   # .items() gives key AND value
        if sal > 30000:
            result[name] = sal
    return result                    # outside the loop, so ALL rows are checked


# Style 2: dict comprehension. Python builds the container for you.
def high_earners_v2(emps):
    return {n: s for n, s in emps.items() if s > 30000}


# print shows on screen. return hands a value back. No return gives None.
def show(emps):
    for name, sal in emps.items():
        if sal > 30000:
            print(name, sal)


print(high_earners(emps))     # {'Manoj': 50000}
print(high_earners_v2(emps))  # {'Manoj': 50000}

x = show(emps)                # prints: Manoj 50000
print(x)                      # None (show has no return)

# Below 30000 instead
print({n: s for n, s in emps.items() if s < 30000})   # {'Ann': 29000}
