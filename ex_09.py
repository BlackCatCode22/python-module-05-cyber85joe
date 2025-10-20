fname = input("Enter file name: ")
if len(fname) < 1 : fname = "romeo.txt"
handle = open(fname)

di = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

print(di)

#now we want to find the most common
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k #cature/remember the word that was largest
print(theword,largest)