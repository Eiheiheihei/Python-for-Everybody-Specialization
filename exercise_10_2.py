#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
fh = open(name)
counts = dict()
temp = list()
for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        t = line[5]
        hrsplt = t.split(":")
        hr = hrsplt[0]
        counts[hr] = counts.get(hr,0)+1

for k,v in sorted(counts.items()):
    print (k,v)
