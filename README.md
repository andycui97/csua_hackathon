# Bookshelf
Authors: Mehdi Kazi, Andy Cui, Oliver Dong, Alex Krentsel

# Description

This code encrypts text into the RGB values for each pixel in the image in such a way that it is not visibile to the human eye, but can be decrypted to recover the original text. The decryption requires a key provided by the encryptor. If the key is lost, the text is unrecoverable.

The demo application of this code encrypts the entire text of books into the image of their cover, which can then be decrypted on any device provided that you have the key generated at encryption. 

Written in Python, along with CSS and HTML for the front end. Output files must be .png images. 

Currently in progress: <br>
<ul>
<li>Huffman Encoding to compress text before encryption and then decompress it after. Based on initial test runs, this cuts down thenumber of bytes by 45%.
</ul>

# Required Libraries

1) [Pillow 3.0.0](https://pypi.python.org/pypi/Pillow/3.0.0) <br>
2) [Cryptography 1.2](https://cryptography.io/en/latest/)

# Source Files

1) csua_frontend - All required files for the front end. <br>
2) cat.jpg - Test file for input. <br>
3) frontend.py - No longer supported. <br>
4) open_read_file.py - Provides reading and writing to files. <br>
5) secret.txt - Sample input file. <br>
6) steno.py - Main stenography file. Self prompting - run through command line. <br>
7) unsteno.py - Main reverse stenography file. Self prompting - run through command line.
