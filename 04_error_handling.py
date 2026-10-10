"""Topic 4: try / except / finally (PL/SQL EXCEPTION block)."""

# Wrong error name = not caught. Name after except must match what Python raises.
try:
    n = int("abc")            # raises ValueError
except ValueError:
    print("Bad number")
finally:
    print("Done")             # finally always runs

# TypeError = wrong type. ValueError = right type, wrong value.
try:
    x = "Total: " + 500       # TypeError
except TypeError:
    print("Fix: 'Total: ' + str(500) ->", "Total: " + str(500))

# try INSIDE the loop: a bad row is skipped, the loop continues.
result = {}
try:
    with open("emps_bad.txt") as f:
        for line in f:
            name, sal = line.strip().split(",")
            try:
                if int(sal) > 30000:
                    result[name] = int(sal)
            except ValueError:
                print("Bad row:", name)
except FileNotFoundError:
    print("File missing")

print(result)   # {'Manoj': 50000, 'Raj': 35000}
