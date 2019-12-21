FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /python
WORKDIR /python
COPY requirements.txt /python/
RUN pip install -r requirements.txt
COPY . /python/
