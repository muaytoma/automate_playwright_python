# Example Dockerfile
FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /app

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
