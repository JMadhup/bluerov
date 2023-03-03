lines = []
with open("waypoint.txt", "r") as f:
    for line in f:
        parts=line.strip().split()
        print(float(parts[1]))