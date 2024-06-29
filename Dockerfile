# Use the official Playwright Docker image
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

# Set working directory
WORKDIR /app

# Update pip to the latest version
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its dependencies
RUN playwright install-deps
RUN playwright install

# Copy the application code into the container
COPY . .

# Command to run the tests and generate HTML report
CMD ["pytest", "app/test_example.py", "--html=/app/output/report.html"]
