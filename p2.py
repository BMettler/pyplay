#!/usr/bin/env python
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

filename = "c:\\win\\sys\\met.exe"
print filename[0]
print filename[1]
print filename[-2]
print filename[3:6]
print filename[3:]
print filename[-3:]
print filename.split("\\")
print filename.split(".")
#c
#:
#x
#win
#win\sys\met.exe
#exe
#['c:', 'win', 'sys', 'met.exe']
#['c:\\win\\sys\\met', 'exe']

#String concatenation 
mail = "b" + "@" + "mail.com"
print mail
mail += " this is an email"
print mail
mail = "".join([mail," - and it is a string"])
print mail

#b@mail.com
#b@mail.com this is an email
#b@mail.com this is an email - and it is a string

#lists
alist = []
alist.append("brandon")
print alist
alist.append("weston")
print alist 
alist.append("raegan")
alist.remove("weston")
alist.append("dog")
alist.append("cat")
print alist
print alist[1]
alist.sort()
print alist
blist= ["house","car","bike"]
newlist = alist + blist
print newlist


#I think this is a tuple .. it is. 
# Once defined, it cant be changed
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

def doerror(someval):
	try:
		x = int(someval)
	except Exception as e:
		print "oops.. [" + str(e) +"]"
		return
	print "just to see if I get here, i shouldnt if error"
doerror("asdasdasd")
	
print "Function returned: [" + str(myfunction(1234)) + "]"

if (3 in ar) and 4 in ar:	 print "3 and 4 is in our array"

if 16 not in ar: print "16 isnt in the ar"

if "c" in "hffrdsaxfcjh" and "z" not in "hffrdsaxfcjh": print "we found c, but not z"

#



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

import os
# or import os as * 
# potential namespace issues.. but dont have to write os.whatever

print str(os.geteuid()) 
print os.listdir("./")
print os.stat("./file.txt") 
print os.system("ls")

osfiles = os.popen("find -f /tmp/*")
print osfiles.readline()

import sys

print "show my sys"
print sys.platform  
# only wiwnsows... sys.getwindowsversion()
print >> sys.stderr, "Error.. blah"


drrfile = open("/etc/passwd")
for line in drrfile:
	#print line
	username = line.split(":")
	if len(username)> 1: 
		#print int(username[2])
		if ( int(username[2]) == 0): 
			print "priv user !!!!!!!!!!!!!!!!!!!!!!!!!!!!" + username[0]

#grab an argument 

if sys.argv[1:]:
	print "got arguments"
	for myarg in sys.argv:
		print myarg


sys.exit()





