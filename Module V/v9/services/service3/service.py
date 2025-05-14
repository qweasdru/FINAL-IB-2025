import socket
import re

FLAG = "blackastra{sRosEbgqKTkFZ6zJ}"

intro = """╭──[ CODE LOCKED ]────╮
│ 🧬 Pattern anomaly  │
│ » Needs number      │
│ » Keyword "mx"      │
│ » SHOUT conclusion! │
╰─────────────────────╯
"""

s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen()
while True:
    c, a = s.accept()
    c.send(intro.encode())
    data = c.recv(1024).decode().strip()
    if re.match(r'^\d{2}.*matrix.*[A-Z]{4}$', data):
        c.send(f"🧩 Matrix verified. FLAG: {FLAG}\n".encode())
    else:
        c.send("⛔ CODE DENIED. Try stronger shout.\n✴ hint: numbers... then something to decode the Matrix?\n".encode())
    c.close()
