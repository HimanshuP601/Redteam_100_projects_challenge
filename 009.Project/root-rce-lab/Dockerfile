FROM python:3.10-slim

# Install ping
RUN apt update && apt install -y iputils-ping

# Install Flask
RUN pip install flask

# Copy app
WORKDIR /app
COPY app/ /app

# RUN AS ROOT (INTENTIONAL)
USER root

EXPOSE 5000
CMD ["python3", "app.py"]

