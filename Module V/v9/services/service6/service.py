import socket

FLAG = "blackastra{YuMzrQjxdrixooX7}"

intro = """ORACLE QUERY ONLINE
-------------------------------
• To pass, speak in the machine tongue.
• Eight bits. One truth.

  What binary unlocks the Oracle?

  Hint: Try 8 bits of B
-------------------------------
"""

def is_correct(bits):
    if len(bits) != 8 or not all(c in '01' for c in bits):
        return False
    return int(bits, 2) == 66  # 66 = ASCII "B"

s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen()

while True:
    c, a = s.accept()
    c.send(intro.encode())
    data = c.recv(1024).decode().strip()
    if is_correct(data):
        c.send(f"Accepted: FLAG — {FLAG}\n".encode())
    else:
        c.send("Rejected. Try again.\n".encode())
