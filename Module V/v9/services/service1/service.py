import socket, base64

FLAG = "blackastra{WpXTEiKjiv02Or4C}"

def decode_logic(blob):
    try:
        # Remove all non-base64 characters
        cleaned = ''.join(filter(lambda x: x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=', blob))
        decoded = base64.b64decode(cleaned + '=' * ((4 - len(cleaned) % 4) % 4)).decode()
        return ''.join([chr(((ord(c)-97-4)%26+97)) for c in decoded.lower() if c.isalpha()])
    except:
        return ""

expected = decode_logic("c_3R;pc#ndp.d}2|VxaXN:0aXJ3aXdl:cWk=")

prompt = """╔═══ ✷ INTERSTELLAR GARBAGE NODE ✷ ═══╗
║ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ▒║
║ > Transmission interfered...       ║
║ > Signal corrupted by debris       ║
║                                     ║
║  ☄ DATA: c_3R;pc#ndp.d}2|VxaXN:0aXJ3aXdl:cWk=            ║
║                                     ║
║ HINT: not all that shines decodes. ║
║       isolate the essence.         ║
╚═════════════════════════════════════╝
> Awaiting decoded payload:
"""

s = socket.socket()
s.bind(("0.0.0.0", 1337))
s.listen()

while True:
    c, a = s.accept()
    c.send(prompt.encode())
    data = c.recv(1024).decode().strip()
    if data == expected:
        c.send(f"🌐 Link confirmed. Flag: {FLAG}\n".encode())
    else:
        c.send("✖ Invalid core signature. Transmission denied.\n".encode())
    c.close()
