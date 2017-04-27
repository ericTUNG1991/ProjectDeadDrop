import sys, getopt, rsa
# from Crypto.PublicKey import RSA
# handling cmdline args
def getCmdLineArgs(argv):
	publicDir = ''
	privateDir = ''
	try:
		opts, args = getopt.getopt(argv, None, ["pub=", "pvt="])
		for opt,arg in opts:
			if(opt == '--pub'):
				publicDir = arg
			elif(opt == '--pvt'):
				privateDir = arg
			else:
				print('usage: python keygen.py --pvt <private key full path> --pub <public key full path>')
	except getopt.GetoptError:
		print('usage: python keygen.py --pvt <private key full path> --pub <public key full path>')
		sys.exit(2)

	return (publicDir, privateDir)


def main():
	# command line arguments
	publicDir, privateDir = getCmdLineArgs(sys.argv[1:])

	# for debugging arguments
	print(publicDir + '\n' + privateDir)


	# key = RSA.generate(2048)

	# ---- developers proceed from here ----
	(pubkey, privkey) = rsa.newkeys(2048, poolsize=4)

	pk = pubkey.save_pkcs1(format = 'PEM')
	pvk = privkey.save_pkcs1(format = 'PEM')

	temp = ""
	with open('pub.pem', 'w') as f:
		f.write(pk)

	# with open('pub.pem','r') as f:
	# 	temp = f.read()
	#
	# pub = rsa.PublicKey.load_pkcs1(temp)
	#
	# print pub
	# print "-----------------------"
	# print pubkey
	#




	with open('pvt.pem', 'w') as f:
		f.write(pvk)

	# temp2 = ""
	# with open('pvt.pem','r') as f:
	# 	temp2 = f.read()
	#
	# p = rsa.PrivateKey.load_pkcs1(temp2)
	#
	# print "-----------------------"
	# print "-----------------------"
	# print p
	# print "-----------------------"
	# print privkey



main()
