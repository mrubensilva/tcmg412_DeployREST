# Init Alpine base image (small Linux distro)
FROM python:3.9-alpine
# Update pip
RUN pip install --upgrade pip
# Set working directory
WORKDIR /code
# Copy contents into WORKDIR
ADD . /code
# Install dependencies
RUN pip install -r requirements.txt
# Start container app
CMD ["python", "app.py"]
