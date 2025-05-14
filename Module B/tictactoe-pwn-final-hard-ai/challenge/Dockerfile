FROM python:3.10-slim

RUN apt update && apt install -y socat && rm -rf /var/lib/apt/lists/*

COPY server.py /home/server.py
COPY game.py /home/game.py
COPY flag.txt /home/flag.txt

RUN chmod +x /home/server.py /home/game.py

EXPOSE 1337
CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /home/server.py"
