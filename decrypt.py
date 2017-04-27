# -author:
# -script: decrypt.py
# -purpose: This script takes in 2048-bit RSA private key either from stdin or from a file, along with
# 	an encrypted message from stdin. The message is converted to plaintext using the key and printed to stdout.

import sys, getopt, rsa, ast, base64
from rsa import DecryptionError

# handling cmdline args
def getCmdLineArgs(argv):

	pvtkeyfile = None
	ciphertextfile = None
	ciphertext = None
	try:
		opts, args = getopt.getopt(argv, None, ["pvtkeyfile=", "ciphertextfile=", "ciphertext="])
		for opt,arg in opts:
			if(opt == '--pvtkeyfile'):
				pvtkeyfile = arg
			elif(opt == '--ciphertextfile'):
				ciphertextfile = arg
			elif(opt == '--ciphertext'):
				ciphertext = arg
			else:
				printUsage()
	except getopt.GetoptError:
		printUsage()
		sys.exit(2)

	return (pvtkeyfile, ciphertextfile, ciphertext)

def printUsage():
	print('usage: python decrypt.py --pvtkeyfile <path to .dat file> --ciphertextfile <path to ciphertext>')

def main():
	# command line arguments
	pvtkeyfile, ciphertextfile, ciphertext = getCmdLineArgs(sys.argv[1:])

	# for debugging arguments
	# print 'pvtkey=' + pvtkey + '\n' + 'pvtkeyFile=' + pvtkeyFile + '\n' + 'ciphertext=' + ciphertext + '\n'

	# ---- developers proceed from here ----
	#
	prkey = ""
	if pvtkeyfile == None or (ciphertextfile == None and ciphertext == None):
		printUsage()
		sys.exit(2)

	# GET RID OF ENDLINES IN MESSAGE AND PUBLIC KEY, remove PEM tags for pubkey literal

# base 64 encoding

	ctext_b64 = ciphertext
	if(ciphertextfile != None):
		with open(ciphertextfile,'rb') as cfile:
			ctext_b64 = cfile.read()
			cfile.close()
	ctext = base64.b64decode(ctext_b64)	

#	print ctextb
	# from file
	keydata = ""
	with open(pvtkeyfile,'rb') as pvtfile:
		keydata = pvtfile.read()
		pvtfile.close()

#	print keydata

	# if(enctext != ctext):
	# 	print "Hello World"

	prkey = rsa.PrivateKey.load_pkcs1(keydata, format ='PEM')

	#make sure right key
	# print keydata
	#
	try:
		decryptedtext = rsa.decrypt(ctext,prkey)
		print(decryptedtext)
		exit(0)
	except (DecryptionError) as e:
		print "Failed to decrypt."
		exit(1)
	# Developer will > outputfile the following:
	# print decryptedtext

main()
