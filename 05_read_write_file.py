"""Topic 5: read emps.txt, write high earners (above 40000) to high.txt."""

# Open BOTH files once, outside the loop.
# "w" erases the file every time it is opened, so never open it inside the loop.
with open("emps.txt") as f, open("high.txt", "w") as out:
    for line in f:
        name, sal = line.strip().split(",")
        if int(sal) > 40000:
            out.write(f"{name},{sal}\n")   # write() takes ONE string; \n ends the line

# high.txt now contains:
# Manoj,50000
