## python studys

#simple if
if (1==1):
	print "bla" + "arg"
elif (2==2):
	print "bla2"
else:
	print "bla3"

thisint = 0
ar = [1,2,3,4,5,6] ## this isnt an array, it is a LIST!!
list = ar 
strar = ["1","2","3","4","5"]

#I think this is a tuple 
tup = ("a","b","c","d")

for mystr in tup:
	print "my str should be [" + mystr + "]"
for myint in ar:
	if myint == 2:
		continue
	print "myint [" + str(myint) + "]"

print "the length of tup is [" +str(len(tup)) +"]"

i=0
while i < 8 :
	i = i + 1
	if i > 1 and i< 3 or i == 6:
		print "i must be two or 6 [" + str(i) + "]"
	print "my i [" + str(i) +"]"

def myfunction(thisint):   ## odd, dont need to call it an int
	print "I Got an int [" + str(thisint) +"]"
	myfunc2(123)
	return 1

def myfunc2(anotherint):
	#lets just try to print thisint
	print "thisint[" + str(thisint) +"]"

print "Function returned: [" + str(myfunction(1234)) + "]"

if (3 in ar) and 4 in ar:	 print "3 and 4 is in our array"

if 16 not in ar: print "16 isnt in the ar"

if "c" in "hffrdsaxfcjh" and "z" not in "hffrdsaxfcjh": print "we found c, but not z"

## fully figure out lists and tuples.. and dictionaries 

handle = file("file.txt")

for line in handle.readlines():
	line = line.rstrip()
	print line

print "doner"

while handle.readline():
	print handle.readline()

print hex(1) ## just returns 0x1.. need to figire out how to do this for other things too..

print ord("A") ## get 65.. not sure, thought it would be a 41

	





