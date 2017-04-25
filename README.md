# CrackVNC
This is a poc code which I wrote to crack the VNC password of TightVNC. 
  
  Command to run   
  
  python crackVNC.py <passwordList.txt>
  
  
  You would need to replace the challenge & reponse which you have captured using wireshark in the main file  
  
  Format  
  challenge = '\xa7\x13\xf5\x0b\x05\x18\xd1\xff\xd9\xceX\xaaO@\xbc\x8e'  
  resposne = "\x80\x89Il>\x9b\x1fD'\x0c\xab\xcf\xacZ\x00\xd8"
 
 
 
 Future plan
 
 Take .pcapng file irectly as input.
