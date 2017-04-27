# -author:
# -script: encrypt.py
# -purpose: This script takes in 2048-bit RSA public key either from stdin or from a file, along with
# 	a message from stdin. The message is converted to ciphertext using the key and printed to stdout.

import sys, getopt, rsa, base64

# handling cmdline args
def getCmdLineArgs(argv):

	pubkeyfile = None
	plaintext = ''
	try:
		opts, args = getopt.getopt(argv, None, ["pubkeyfile=", "plaintext="])
		for opt,arg in opts:
			if(opt == '--pubkeyfile'):
				pubkeyfile = arg
			elif(opt == '--plaintext'):
				plaintext = arg
			else:
				print 'usage: python encrypt.py --pubkeyfile <path to file> --plaintext <plaintext>'
	except getopt.GetoptError:
		print 'usage: python encrypt.py --pubkeyfile <path to file> --plaintext <plaintext>'
		sys.exit(2)

	return (pubkeyfile, plaintext)

def main():
	# command line arguments
	pubkeyfile, plaintext = getCmdLineArgs(sys.argv[1:])
	#
	pukey = ""
	if pubkeyfile == None:
		print 'usage: python encrypt.py --pubkeyfile <path to file> --plaintext <plaintext>'
		sys.exit(2)

	# GET RID OF ENDLINES IN MESSAGE AND PUBLIC KEY, remove PEM tags for pubkey literal

	# from file
	keydata = ""

	with open(pubkeyfile,'rb') as pubfile:
		keydata = pubfile.read()

	pukey = rsa.PublicKey.load_pkcs1(keydata, format ='PEM')

	#make sure right key
	# print keydata

	plaintext = plaintext.encode('utf-8')

	ciphertext = rsa.encrypt(plaintext,pukey)
	ciphertext_b64 = base64.b64encode(ciphertext)

	print ciphertext_b64
	exit(0)

	#with open("ciphertext.txt","w") as ctext:
	#	ctext.write(ciphertext)

	# Developer will > outputfile the following:


# Multiple widgets problem


	# for debugging arguments
	# print 'pubkey=' + pubkey + '\n' + 'pubkeyFile=' + pubkeyFile + '\n' + 'plaintext=' + plaintext + '\n'

	# ---- developers proceed from here ---


main()
