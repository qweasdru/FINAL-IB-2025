#!/usr/bin/env python3
import sys
import game

class SocketWrapper:
    def __init__(self):
        self.stdin = sys.stdin
        self.stdout = sys.stdout

    def recv(self, size=1024):
        return self.stdin.readline().encode()

    def sendall(self, data):
        self.stdout.write(data.decode())
        self.stdout.flush()

if __name__ == "__main__":
    try:
        conn = SocketWrapper()
        g = game.Game(conn)
        g.play()
    except SystemExit:
        pass
    except Exception as e:
        sys.stdout.write("\n[!] Error occurred.\n")
        sys.stdout.flush()
