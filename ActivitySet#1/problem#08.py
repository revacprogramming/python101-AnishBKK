# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    l = (line.find("0"))
    n = (float(line[l:l+7]))
    tot = float(tot + n)
    count = float(count + 1)
  
avg = float(tot/count)
print("Average spam confidence:",avg)