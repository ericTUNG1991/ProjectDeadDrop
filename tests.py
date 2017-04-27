import subprocess
from subprocess import call, check_output

test_msg = "mymsgyolololo"
pvtkey_fname = "pvt.pem"
pubkey_fname = "pub.pem"
url = "http://vertigo.cs.umd.edu/testDigiDrop.php"

#
# -Basic test for keygen, encrypt, decrypt
# 1. generate keys
# 2. encrypt plaintext into ciphertext
# 3. decrypt the same ciphertext back into plaintext
# 4. check if the message is the same
def test0():
	subprocess.call('python keygen.py', shell=True)
	encrypt_output = check_output(["python", "encrypt.py", "--pubkeyfile", pubkey_fname, "--plaintext", test_msg]).strip()

	assert (test_msg != encrypt_output)

	decrypt_output = check_output(["python", "decrypt.py", "--pvtkeyfile", pvtkey_fname, "--ciphertext", encrypt_output]).strip()

	assert (test_msg == decrypt_output)
	print 'test0 completed successfully'

#
# -More in depth test for keygen, encrypt, decrypt, putmsg, getmsg
# 1. generate keys
# 2. encrypt plaintext into ciphertext
# 3. place ciphertext onto website containing DigiDrop widget using putmsg
# 4. retrieve ciphertext from website and decrypt back into plaintext using getmsg
# 5. check if the decrypted text equals the original message after being uploaded to and downloaded from widget
def test1():
	subprocess.call('python keygen.py', shell=True)
	encrypt_output = check_output(["python", "encrypt.py", "--pubkeyfile", pubkey_fname, "--plaintext", test_msg]).strip()
	subprocess.call('python putmsg.py --url %s --msg %s' % (url, encrypt_output), shell=True)
	getmsg_output = check_output(['python', 'getmsg.py', '--pvtkeyfile', pvtkey_fname, '--url', url]).strip()

	assert (test_msg == getmsg_output)
	print 'test1 completed successfully'

#
# -testing keygen, encrypt, decrypt, putmsg, getmsg, qrread, qrwrite
# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
def test2():
	print ""

def main():
	test0()
	test1()

main()
