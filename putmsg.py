# -author:
# -script: putmsg.py
# -purpose: takes in a url and encrypted message from stdin and attempts to place it on a website
#	containing a DigiDrop widget

import sys, getopt
import requests
import mechanize
import time

# handling cmdline args
def getCmdLineArgs(argv):
	url = None
	msg = None
	msgfile = None
	try:	
		opts, args = getopt.getopt(argv, None, ["url=", "msg=", "msgfile="])
		for opt,arg in opts:
			if(opt == '--url'):
				url = arg	
			elif(opt == "--msg"):
				msg = arg 
			elif(opt == "--msgfile"):
				msgfile = arg
			else:
				print 'usage: python putmsg.py --url <url of website to post on> --msg <message to post>'
	except getopt.GetoptError:
		print 'usage: python putmsg.py --url <url of website to post on> --msg <message to post>'
		sys.exit(2)

	return (url, msg, msgfile)

def main():
	# command line arguments
	url, msg, msgfile = getCmdLineArgs(sys.argv[1:])

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
			br["DigiDropMessageInput"] = msg
		elif (msgfile is not None):
			print "inside msgfile"
			try:
				f_open = open(msgfile, 'r')
				line_spl = f_open.read()
			except (OSError, IOError) as e:
				print "Not valid filename"
				exit(0)
		
			f_open.close()
		
			output = line_spl
			#print "The msg is: " + str(output)
			br["DigiDropMessageInput"] = str(output)

		res = br.submit()
	except mechanize.FormNotFoundError as e:
		print "Website does not support DigiDrop functionality"
		#import traceback
		#traceback.print_exc(file=sys.stdout)
		#print e
	




main()
 




