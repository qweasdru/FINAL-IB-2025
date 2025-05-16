
FROM ubuntu:20.04

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y socat gcc

WORKDIR /home/app

COPY chall.c flag.txt Makefile ./

RUN make

EXPOSE 1338

CMD ["socat", "TCP-LISTEN:1338,reuseaddr,fork", "EXEC:/home/app/chall,stderr"]
