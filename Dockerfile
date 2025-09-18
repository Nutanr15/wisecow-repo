FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y cowsay fortune-mod netcat && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY wisecow.sh /app/wisecow.sh
RUN chmod +x /app/wisecow.sh
ENV SRVPORT=4499
ENV PATH="/usr/games:${PATH}"
EXPOSE 4499
ENTRYPOINT ["/app/wisecow.sh"]
