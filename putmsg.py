# -author:
# -script: putmsg.py
# -purpose: takes in a url and encrypted message from stdin and attempts to place it on a website
#	containing a DigiDrop widget

import sys, getopt
import requests
import mechanize
import time
import codecs
import subprocess

# handling cmdline args
def getCmdLineArgs(argv):
	url = None
	msg = None
	msgfile = None
	pubkeyfile = None
	try:
		opts, args = getopt.getopt(argv, None, ["url=", "msg=", "msgfile=", "pubkeyfile="])
		for opt,arg in opts:
			if(opt == '--url'):
				url = arg
			elif(opt == "--msg"):
				msg = arg
			elif(opt == "--msgfile"):
				msgfile = arg
			elif(opt == "--pubkeyfile"):
				pubkeyfile = arg
			else:
				print 'usage: python putmsg.py --url <url of website to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>'
	except getopt.GetoptError:
		print 'usage: python putmsg.py --url <url of website to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>'
		sys.exit(2)

	return (url, msg, msgfile, pubkeyfile)

def main():
	# command line arguments
	url, msg, msgfile, pubkeyfile = getCmdLineArgs(sys.argv[1:])


	if url == None or (msg == None and msgfile == None) or pubkeyfile == None:
		print 'usage: python putmsg.py --url <url of website to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>'
		sys.exit(2)


	# for debugging arguments
	# print 'url= ' + url + '\n' + 'msg= ' + msg + '\n'

	# ---- developers proceed from here ----
	# test = requests.get(url)
	# test.encoding = 'ISO-8859-1'
	# r = requests.post(url + "POST", data=msg)
	# print r.text
	br = mechanize.Browser()
	br.open(url)
	try:

		br.select_form(name="DigiDropForm")
		output = ''
		if (msg is not None):
			script_cmd = 'python encrypt.py --pubkeyfile %s --plaintext %s' % (pubkeyfile, msg)
			child = subprocess.Popen(script_cmd, stdout=subprocess.PIPE, shell=True)
			stdout_text = child.communicate()[0].strip()
			exit_val = child.returncode
			if(exit_val == 0):
				br["DigiDropMessageInput"] = stdout_text.strip()
			else:
				print "Could not encrypt"
				sys.exit(2)
		elif (msgfile is not None):
		#	print "inside msgfile"
			try:
				f_open = open(msgfile, 'r')
				line_spl = f_open.read()
			except (OSError, IOError) as e:
				print "Not valid filename"
				exit(0)

			f_open.close()

			output = line_spl

			script_cmd = 'python encrypt.py --pubkeyfile %s --plaintext %s' % (pubkeyfile, str(output))
			child = subprocess.Popen(script_cmd, stdout=subprocess.PIPE, shell=True)
			stdout_text = child.communicate()[0].strip()
			exit_val = child.returncode
			if(exit_val == 0):
				br["DigiDropMessageInput"] = stdout_text.strip()
			else:
				print "Could not encrypt"
				sys.exit(2)
		else:
			print 'usage: python putmsg.py --url <url of website to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>'
			sys.exit(2)

		res = br.submit()
	except mechanize.FormNotFoundError as e:
		print "Website does not support DigiDrop functionality"
		#import traceback
		#traceback.print_exc(file=sys.stdout)
		#print e





main()
