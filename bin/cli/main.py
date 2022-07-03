#!/usr/bin/env python

import pyscrypt

def hashPsw(password):
    salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
    key = pyscrypt.hash(password, salt, 2048, 8, 1, 32)
    return key.hex()

def comp(psw1, psw2):
    hash1 = hashPsw(psw1)
    hash2 = hashPsw(psw2)
    print( "[COMP] psw1 = %s, psw2 = %s" % (psw1, psw2));
    if hash1 == hash2:
        print( "[COMP] true");
    else:
        print( "[COMP] false");

def printPsw(password):
    print( "[INPUT] %s" % password);
    print( "[OUTPUT] %s" % hashPsw(password));

def main():
    psw1 = b'pass123'; # b turns this string into a byte array
    psw2 = b'123pass';
    printPsw(psw1)
    printPsw(psw2)
    comp(psw1, psw1)
    comp(psw1, psw2)

if __name__ == '__main__':
    main()
