FROM ubuntu:22.04

# Install required packages
RUN apt-get update && \
    apt-get install -y cowsay fortune-mod netcat && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the Wisecow script from src folder
COPY src/wisecow.sh /app/wisecow.sh

# Make it executable
RUN chmod +x /app/wisecow.sh

# Set environment variables
ENV SRVPORT=4499
ENV PATH="/usr/games:${PATH}"

# Expose port
EXPOSE 4499

# Start the application
ENTRYPOINT ["/app/wisecow.sh"]

