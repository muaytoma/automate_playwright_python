# Start from the official Jenkins LTS image
FROM jenkins/jenkins:lts

# Switch to the root user to install packages
USER root

# Install Python, pip, and virtualenv
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon-x11-0 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libpango1.0-0 \
    libcairo2 \
    libasound2 \
    wget \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a directory for the virtual environment
RUN mkdir -p /opt/venv

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv

# Install Playwright in the virtual environment
RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install playwright && \
    /opt/venv/bin/playwright install

# Add the virtual environment to PATH for all users
ENV PATH="/opt/venv/bin:$PATH"

# Revert back to the Jenkins user
USER jenkins

# Set the working directory to Jenkins workspace
WORKDIR /workspace

# Default command is not needed; Jenkins image starts Jenkins automatically
