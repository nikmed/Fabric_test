FROM python:3.8
WORKDIR /fabric_test
COPY requirements.txt /fabric_test
RUN pip3 install -r requirements.txt
COPY . /fabric_test/