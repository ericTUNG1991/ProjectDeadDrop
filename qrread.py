# -author:
# -script: qrread.py
# -purpose: takes in a QR code image file and prints the text contained within the QR code to stdout

import sys, getopt, pyqrcode, qrtools

# handling cmdline args
def getCmdLineArgs(argv):
	qrfile = None
	try:
		opts, args = getopt.getopt(argv,None, ["qrfile="])
		for opt,arg in opts:
			if(opt == '--qrfile'):
				qrfile = arg
			else:
				print 'usage: python qrread.py --qrfile <qr file>'
	except getopt.GetoptError:
		print 'usage: python qrread.py --qrfile <qr file>'
		sys.exit(2)

	return qrfile

def main():
	# command line arguments
	qrfile = getCmdLineArgs(sys.argv[1:])

	if qrfile == None:
		print 'usage: python qrread.py --qrfile <qr file>'
		sys.exit(2)

	# for debugging arguments
	# print 'qrfile=' + qrfile + '\n'

	# ---- developers proceed from here ----

	# package need to install:
	# sudo apt-get install python-zbar
	# pip install pypng
	# pip install Pillow
	#print qrfile

	#sudo pip install pillow -U

	qr = qrtools.QR()
	# print qrfile
	qr.decode(qrfile)

	temp = qr.data


	print temp

main()
