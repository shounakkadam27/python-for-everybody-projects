fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find(':')
        num = float(line[pos+1:])
        total = total + num
        count = count + 1

average = total / count

print("Average spam confidence:", average)



