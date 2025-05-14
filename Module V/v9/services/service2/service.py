import socket

FLAG = "blackastra{EYWCER7IWmY9gjNd}"

intro = """⎧⎯⎯⎯⎯⎯⎯⎯⎯ SUBSPACE RUPTURE ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎫
|                                                |
|   ✴ ERROR 900: Fragment loop in ∅ channel     |
|   ✴ HINT: the only way to stabilize is to      |
|             speak in void tongue: X.Y          |
|                                                |
⎩⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎭
"""

s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen()
while True:
    c, a = s.accept()
    c.send(intro.encode())
    data = c.recv(1024).decode().strip()
    if data.lower() == "void.sync":
        c.send(f"✔️ Void accepted. FLAG: {FLAG}\n".encode())
    else:
        c.send("✖ Instability continues...\nHINT? Perhaps... sync the void?\n".encode())
    c.close()
