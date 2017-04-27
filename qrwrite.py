# -author:
# -script: qrwrite.py
# -purpose: takes in text either from stdin or from a file and writes it to a QR code image

import sys, getopt, pyqrcode, qrtools

# handling cmdline args
def getCmdLineArgs(argv):
	text = None
	textfile = None
	qrfile = None
	try:
		opts, args = getopt.getopt(argv, None, ["text=", "textfile=", "qrfile="])
		for opt,arg in opts:
			if(opt == '--text'):
				text = arg
			elif(opt == '--textfile'):
				textfile = arg
			elif(opt == '--qrfile'):
				qrfile = arg
			else:
				print 'usage: python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>'
	except getopt.GetoptError:
		print 'usage: python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>'
		sys.exit(2)

	return (text, textfile, qrfile)

def main():
	# command line arguments
	text, textfile, qrfile = getCmdLineArgs(sys.argv[1:])

	if qrfile == None or (textfile == None and text == None):
		print 'usage: python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>'
		sys.exit(2)

	# for debugging arguments
	# print 'text=' + text + '\n' + 'textfile=' + textfile + '\n' + 'qrfile=' + qrfile + '\n'

	# ---- developers proceed from here ----

	# if text is not None, it will the key text to QR

	if text == None or text == "":
		if textfile != None:
			text = ""
			with open(textfile, 'r') as readfile:
				for line in readfile:
					#if not "-----" in line:
					text = text + line
			readfile.close()

	if text != None and text != "":
		img = pyqrcode.create(text)
		img.png(qrfile, scale=2)
	else:
		print "Error: Empty Input"
		print 'usage: python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>'
		sys.exit(2)


	# if text is None and textfile is not None, it will read
	# through textfile and convert it to QR






main()
