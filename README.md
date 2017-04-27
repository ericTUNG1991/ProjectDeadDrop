# ProjectDeadDrop

#HOW TO USE

# Step 1 Generating Keys

$ python keygen.py

This generates a public and private key file (pub.pem and pvt.pem). Now users will trade public key with intended recipent. ONLY call keygen.py once otherwise public keys will need to be traded again.



# Step 2 Trading Public Keys
Initial public key trading is left up to users. We do provide a method of public key trading as an example using QR codes.


# Step 3 Encryption

$ python encrypt.py --pubkeyfile <path to file> --plaintext <plaintext>

User will encrypt their plain text message through the command line using encrypt.py. The user will use their senders pub.pem file as the public key. The user can save the message to a file using command line or create a message via QR code using our qrwrite.py. 

$ python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>

Alternatively, users can send messages via our widget using putmsg.py.

$ python putmsg.py --url <url of website with widget to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>

# Step 4 Decryption 

$ python decrypt.py --pvtkeyfile <path to file> --ciphertextfile <path to ciphertext> OR --ciphertext <ciphertext literal>

Receivers can decrypt the senders message via command line using the above command. The receiver will need to use their own private key, pvt.pem file created during Step 1. If the user received a QR image they can use qrread.py to get the encrypted message and/or public key

$python qrread.py --qrfile <qr file>

Alternatively, users can receive and decrypt messages via our widget using getmsg.py.

$ python getmsg.py --url <url of website to pull from> --pvtkeyfile <path to pvt key file>





#script details

#encrypt.py 
#usage: python encrypt.py --pubkeyfile <path to file> --plaintext <plaintext>

#decrypt.py
#usage: python decrypt.py --pvtkeyfile <path to file> --ciphertextfile <path to ciphertext> OR --ciphertext <ciphertext literal>

#getmsg.py
#usage: python getmsg.py --url <url of website to pull from> --pvtkeyfile <path to pvt key file>

#putmsg.py
#usage: python putmsg.py --url <url of website to post on> --msg <message to post> OR --msgfile <path to file> --pubkeyfile <path to file>

#qrread.py
#usage: python qrread.py --qrfile <qr file>

#qrwrite.py
#usage: python qrwrite.py --textfile <path to file> OR --text <message to convert> --qrfile <qr file>



# additional notes
# must escape spaces in message with "\" for put/getmsg scripts
