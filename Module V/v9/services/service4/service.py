import socket, base64, hashlib

FLAG = "blackastra{emVu1NRYzdUeHCxm}"
KEYWORD = "launchcode"

intro = """ LINK PROTOCOL: ALPHA CORE

  > initiate launch sequence
  > validate encrypted call tag
  > double-encoded form required

  HINT: cold digest, then wrap tight.

"""


s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen()
while True:
    c, a = s.accept()
    c.send(intro.encode())
    data = c.recv(1024).decode().strip()
    try:
        if data == base64.b64encode(hashlib.sha256(KEYWORD.encode()).hexdigest().encode()).decode():
            c.send(f" DECRYPTION SUCCESS  FLAG: {FLAG}\n".encode())
        else:
            c.send(b" INVALID TRANSMISSION\n Are you hashing cold enough?\n")
    except:
        c.send(b" ERROR\n")
    c.close()
