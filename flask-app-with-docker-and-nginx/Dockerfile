FROM python:3

# set a directory for the app
WORKDIR /usr/src/app

# install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy all the files to the container
COPY . .

# tell the port number the container should expose
EXPOSE 6001

# run the command
CMD ["python", "./app.py"]