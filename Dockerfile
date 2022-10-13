# Init Alpine base image (small Linux distro)
FROM python:3.6.1-alpine
# Update pip
RUN pip install --upgrade pip
# Set working directory
WORKDIR /DeployREST
# Copy contents into WORKDIR
ADD . /DeployREST
# Install dependencies
RUN pip install requests
RUN pip install Flask
RUN pip install slackeventsapi
# Start container app
CMD ["python", "DeployRestFinal.py"]