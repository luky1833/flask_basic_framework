FROM py:36

# Set the working directory to /app
WORKDIR /opt/es_automatic_alarm

# Copy the current directory contents into the container at /app
COPY ./hosts /etc/hosts
COPY . /opt/es_automatic_alarm

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip3 install requests
# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
#ENV NAME World

# Run app.py when the container launches
CMD ["python3", "/opt/es_automatic_alarm/app.py"]