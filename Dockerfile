# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcb-dri3-0 \
    libdrm2 \
    libgbm1 \
    libxcomposite1 \
    libxrandr2 \
    libxi6 \
    libxcursor1 \
    libxdamage1 \
    libxkbcommon0 \
    libgl1-mesa-glx \
    libpango-1.0-0 \
    libcups2 \
    libcairo2 \
    libxshmfence1 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    libevent-2.1-7 \
    libx11-xcb-dev \
    libdbus-1-3 \
    libxtst6 \
    libxrandr2 \
    libasound2 \
    libatspi2.0-0 \
    libgbm-dev \
    libnss3-tools 

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN playwright install-deps
RUN playwright install

# Copy the current directory contents into the container at /app
COPY . .

# Command to run the tests and generate HTML report
CMD ["pytest"]