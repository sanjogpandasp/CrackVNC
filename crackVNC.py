import pyDes
import sys

class RFBDes(pyDes.des):
    def setKey(self, key):
        """RFB protocol for authentication requires client to encrypt
           challenge sent by server with password using DES method. However,
           bits in each byte of the password are put in reverse order before
           using it as encryption key."""
        newkey = []
        for ki in range(len(key)):
            bsrc = ord(key[ki])
            btgt = 0
            for i in range(8):
                if bsrc & (1 << i):
                    btgt |= 1 << 7 - i
            newkey.append(chr(btgt))
        super(RFBDes, self).setKey(newkey)
        #print "Done with RFDDes fucntion."


def decode(challenge, response, pfile):

  
    #print "Done with _init_ fucntion"
    with open(pfile, 'r') as plist:
        for password in plist:
            password = password.strip('\n')
            key = (password + '\0' * 8)[:8]
            actualKey = RFBDes(key)
            output = actualKey.encrypt(challenge)
            #print output
            if output == response:
                print "Password cracked is " + key


if __name__ == '__main__':


    challenge = '\xa7\x13\xf5\x0b\x05\x18\xd1\xff\xd9\xceX\xaaO@\xbc\x8e'
    response = "\x80\x89Il>\x9b\x1fD'\x0c\xab\xcf\xacZ\x00\xd8"
    pfile = sys.argv[1]
    decode(challenge, response, pfile)
