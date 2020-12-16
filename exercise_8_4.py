#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for wrd in line:
        if wrd not in lst:
            lst.append(wrd)
            #这一条要搞了一个小时，本来写的 lst = lst.appen(wrd)，一直出来报错
lst.sort()
#这里也是一样， lst = lst.sort()就不对，出不来东西
print(lst)
