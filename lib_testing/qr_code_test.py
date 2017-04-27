import pyqrcode
import qrtools

text = ""
textfile = "test.pem"
qrfile = "qrCode.png"


if text == None or text == "":
	if textfile != None:
		text = ""
		with open(textfile, 'r') as readfile:
			for line in readfile:
				if not "-----" in line:
					text = text + line
		readfile.close()
if text != None and text != "":
	img = pyqrcode.create(text)
	img.png(qrfile, scale=2)
else:
	print "Error: Empty Input"

qr = qrtools.QR()
qr.decode("qrCode.png")
print qr.data

