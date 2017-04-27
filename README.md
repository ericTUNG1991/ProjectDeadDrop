# ProjectDeadDrop

#HOW TO USE

# Step 1 Generating Keys

# $python keygen.py

# this generates a public and private key file (pub.pem and pvt.pem).
# now user will trade public key with intended recipent.
# ONLY call keygen.py once otherwise public keys will need to be traded again.



# Step 2 Trading Public Keys
# Initial public key trading is left up to users.
# We do provide two methods of public key trading as (QR Codes )

# Basic encryption/decription








#script details

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
