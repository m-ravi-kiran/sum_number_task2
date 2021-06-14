
FROM python:3.9-alpine

# create a directory for the application in the container.
WORKDIR /sum_nums_app

# Copy all the contents of the project to the container.
ADD . /sum_nums_app

# Run all the dependency related commands on the container.
RUN pip3 install -r requirements.txt

# The final command to start the application on the container.
CMD ["python", "api.py"]