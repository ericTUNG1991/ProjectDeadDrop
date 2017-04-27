# ProjectDeadDrop

# HOW TO USE

#encrypt.py 
#usage: python encrypt.py --pubkeyfile <path to file> --plaintext <plaintext>

#decrypt.py
#usage: python decrypt.py --pvtkeyfile <path to file> --ciphertextfile <path to ciphertext> OR --ciphertext <ciphertext literal>

#getmsg.py
#usage: python getmsg.py --url <url of website to pull from> --pvtkeyfile <path to pvt key file>

#putmsg.py
#usage: python putmsg.py --url <url of website to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>

#qrwrite.py
#usage: python qrread.py --qrfile <qr file>

#prwrite.py
#usage: python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>



# additional notes
# must escape spaces in message with "\" for put/getmsg scripts
