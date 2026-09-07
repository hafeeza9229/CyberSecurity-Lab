count = 0

with open("sample.log", "r") as file:
    for line in file:
        if "failed" in line:
            count = count + 1

print("Number of failed login attempts:", count)
