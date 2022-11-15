FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /cartridge
WORKDIR /cartridge
ADD requirements.txt /cartridge/
RUN pip install -r requirements.txt
ADD . /cartridge/
