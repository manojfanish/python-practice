"""Topic 3: read emps.txt and keep salaries above 30000."""

result = {}
with open("emps.txt") as f:                  # "r" (read) is the default mode
    for line in f:                           # one line at a time, like a cursor loop
        name, sal = line.strip().split(",")  # strip removes \n, split cuts at comma
        if int(sal) > 30000:                 # file data is text, so convert first
            result[name] = int(sal)

print(result)   # {'Manoj': 50000, 'Raj': 35000}

# Try changing the filter and predict the output before running:
#   < 30000   -> {'Ann': 29000}
#   <= 35000  -> {'Ann': 29000, 'Raj': 35000}
#   >= 35000  -> {'Manoj': 50000, 'Raj': 35000}
#   == 35000  -> {'Raj': 35000}
#   != 35000  -> {'Manoj': 50000, 'Ann': 29000}
