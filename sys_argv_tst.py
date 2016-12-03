import sys

def readfile(filename):
	'''Print a flie to the standard output'''
	f=file(filename)
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print line,
	f.close()
	
#script start
if len(sys.argv)<2:
	print 'NO action specified'
	sys.exit()

if sys.argv[1].startswith('__'):
	option=sys.argv[1][2:]
	#fetch sys.argv[1]
	if option=='version':
		print 'Verion 1.2'
	elif option=='help':
		print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
--version : Prints the version number
--help : Display this help'''
	else:
		print 'Unknown option'
	sys.exit()
else:
	for filename in sys.argv[1:]:
		readfile(filename)


