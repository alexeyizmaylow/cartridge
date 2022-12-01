FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /cartridge
WORKDIR /cartridge
ADD requirements.txt /cartridge/
RUN pip install -r requirements.txt
ADD . /cartridge/
EXPOSE 8100
CMD python3 manage.py runserver 0.0.0.0:8100
