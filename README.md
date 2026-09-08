About This Project

This is a basic Python script that should show how symmetric and asymmetric encryption works. It takes a short message, encrypts it, and then decrypts it back to the original text. I used the cryptography library so I could focus on how the two methods work instead of trying to create my own encryption algorithm.

How It Works

The script uses the message "Hello, this is my secret message!" for both examples.

For symmetric encryption, I used Fernet. It generates one secret key, and that same key is used to encrypt and decrypt the message.

For asymmetric encryption, I used RSA with OAEP and SHA-256. The script generates a public and private key pair. The public key is used to encrypt the message, and the private key is used to decrypt it.

After both examples run, the script saves the keys, original message, encrypted outputs, and decrypted outputs to results.txt. The encrypted RSA output is shown in Base64 so it can be displayed as readable text. The keys and encrypted outputs will be different each time the program runs because new keys and random encryption values are generated.

How to Run It

Make sure Python is installed, then open a terminal in the project folder and install the required library:
python -m pip install cryptography

Run the script with:

python app.py

The terminal will show whether both examples were successful. Open results.txt to see all the keys, inputs, and outputs. You can also change the MESSAGE variable near the top of app.py to try a different short message.


NOTE: If you want to see the decrypted output, locate the lines of code with the # in front of them
you will see a comment above them telling you what they are