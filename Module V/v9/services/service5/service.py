import socket, hashlib

FLAG = "blackastra{d9QBDcciZPmKZaCL}"

intro = """ SIGMA GATEWAY 
   
    Only value with spiral end opens
    SHA256(???)  endswith '42'
    Solve the trail. Find harmony.
"""

s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen()
while True:
    c, a = s.accept()
    c.send(intro.encode())
    data = c.recv(1024).decode().strip()
    try:
        h = hashlib.sha256(data.encode()).hexdigest()
        if h.endswith("42"):
            c.send(f" Signature aligned. FLAG: {FLAG}\n".encode())
        else:
            c.send(b" Alignment failed.\nHint: the signature... ends in meaning?\n")
    except:
        c.send(b" Error processing input.\n")
    c.close()
