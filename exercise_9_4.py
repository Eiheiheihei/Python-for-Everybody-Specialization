#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
fh = open(name)
counts = dict()


for line in fh:
    if line.startswith("From") and not line.startswith("From:"):
        line = line.split()
        adr = line[1]
        counts[adr] = counts.get(adr,0)+1
        #get这里后面括号里的adr不用加冒号！！！
mp = None
nc = None
#N要大写
for adr,count in counts.items():
    if nc is None or count > nc:
    # 用is，不能用nc=None
        mp = adr
        nc = count

print (mp,nc)
#不用加引号
