# csua_hackathon

# Description

This code encrypts text into the RGB values for each pixel in the image in such a way that it is not visibile to the human eye, but can be decrypted to recover the original text. The decryption requires a key provided by the encryptor. If the key is lost, the text is unrecoverable. 

Written in Python, along with CSS and HTML for the front end. Output files must be .png images. 

# Required Libraries

1) [Pillow 3.0.0](https://pypi.python.org/pypi/Pillow/3.0.0)
2) [Cryptogrphy 1.2](https://cryptography.io/en/latest/)

# Soruce Files

1) csua_frontend - All required files for the front end.
2) cat.jpg - Test file for input.
3) frontend.py - No longer supported.
4) open_read_file.py - Provides reading and writing to files.
5) secret.txt - Sample input file.
6) steno.py - Main stenography file. Self promtping - run through command line.
7) unsteno.py - Main reverse stenography file. Self prompting - run through command line. 
