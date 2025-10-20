fname = input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
handle = open(fname)


many = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        many[w] = many.get(w, 0) + 1

# Find the top 5 word by frequency

print(many.items)

print(sorted((many.items()), key=lambda x: x[1], reverse=True))

tmp = dict()
newlist = list()
for k, v in many.items():
    tuple = (v, k)
    newlist.append(tuple)

cool = (sorted(newlist, reverse=True))
print(cool)

for k, v in cool[:5] :
    print(k, v)



