import sys, getopt, re, requests, os

formRule = '<form.*>.*</form>'
tableRule = '<ul name="DigiDropMessageList">.*</ul>'
msgRule = '(<li>).*(</li>)'
testURL = 'http://vertigo.cs.umd.edu/testDigiDrop.php'


# handling cmdline args
def getCmdLineArgs(argv):
	url = None
	pvtkeyFile = None
	try:
		opts, args = getopt.getopt(argv, None, ["url=", "pvtkeyfile="])
		for opt,arg in opts:
			if(opt == '--url'):
				url = arg
			elif(opt == '--pvtkeyfile'):
				pvtkeyFile = arg
			else:
				print('usage: python getmsg.py --url <url of website to pull from> --pvtkeyfile <path to pvtkeyfile>')
	except getopt.GetoptError:
		print('usage: python getmsg.py --url <url of website to pull from> --pvtkeyfile <path to pvt key file>')
		sys.exit(2)

	return (url, pvtkeyFile)

def main():
	url, pvtkeyFile = getCmdLineArgs(sys.argv[1:])

	if url == None or pvtkeyFile == None:
		print('usage: python getmsg.py --url <url of website to pull from> --pvtkeyfile <path to pvt key file>')
		sys.exit(2)

	r = requests.get(url)
	text = r.text

	# ---- temporarily commenting out ----



	# ---- Begin BeautifulSoup ----

	from bs4 import BeautifulSoup
	import codecs
	import subprocess

	soup = BeautifulSoup(text, 'html.parser')
	msgList = soup.find(id="DigiDropMessageList").children

	for msgListItem in msgList:
		if(msgListItem != None or len(msgListItem.string.strip()) > 0):
			script_cmd = 'python decrypt.py --pvtkeyfile %s --ciphertext %s' % (pvtkeyFile, msgListItem.string)
			child = subprocess.Popen(script_cmd, stdout=subprocess.PIPE, shell=True)
			stdout_text = child.communicate()[0].strip()
			exit_val = child.returncode
			if(exit_val == 0):
				print stdout_text.strip()


	# ---- End BeautifulSoup ----







main()
