# Level 1: Read and skip bad rows. Loop over the file and put valid rows in a dict {name: salary}. 
# For a bad row, print Bad row: Priya and keep going. Remember where the try goes.
def load_staff(filename):
    result={}
    with open(filename) as f:
        for line in f:
            try:
                name,city,salary = line.strip().split(",") 
                result[name] = int(salary)
            except ValueError:
                print(f"Bad row: {name}")
    return result

#Level 2: Make it a function Wrap your code in a function load_staff(filename) that returns the dict instead of printing it. 
# Then call it from outside.
staff = load_staff("staff.txt")
#print(staff)

#Level 3: Statistics 
# Below your function call, using the staff dict it returned, print these four lines:
#Total: 183000
#Average: 36600.0
#Highest: 50000
#Lowest: 28000

total = sum(staff.values())
Average= total/len(staff)
Highest = max(staff.values())
Lowest = min(staff.values())

print(f"Total: {total}")
print(f"Average: {Average}")
print(f"Highest: {Highest}")
print(f"Lowest: {Lowest}")
