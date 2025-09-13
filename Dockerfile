# 1. Use an official lightweight Python runtime as a parent image
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the application files into the container
COPY . .

# 4. Install uv, the fast Python package installer and resolver
RUN pip install uv

# 5. Create a virtual environment in the working directory
# This creates a directory named .venv
RUN uv venv

# 6. Install Python dependencies from requirements.txt into the virtual environment.
# uv automatically detects and uses the .venv in the current directory.
# --no-cache-dir is used to reduce image size.
RUN uv pip install --no-cache-dir -r requirements.txt

# 7. Expose the port the app runs on
EXPOSE 80

# 8. Set environment variable to ensure Python output is sent to the terminal
ENV PYTHONUNBUFFERED=1

# 9. Define the command to run the application.
# This command directly uses the Python executable from the virtual environment.
# We don't use "source .venv/bin/activate" because each Docker command runs
# in a new shell, and the activation would not persist.
CMD [".venv/bin/python3.12", "-u", "app.py"]
