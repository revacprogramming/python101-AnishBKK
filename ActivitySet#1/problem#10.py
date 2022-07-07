#dict_ex9.4
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

maxauth = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    maxauth[words[1]] = maxauth.get(words[1],0)+1

lar = None
larauth = None

for key in maxauth:
    if lar is None: largest = maxauth[key]

    if largest < maxauth[key]:
        largest = maxauth[key]
        largest_author = key

print(larauth, lar)