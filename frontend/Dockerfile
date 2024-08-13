# Use the official Python image
FROM python:3.12

# Set the working directory
WORKDIR /frontend

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire frontend directory
COPY . /frontend

# Expose the port Streamlit runs on
EXPOSE 8501

# Start the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501"]
