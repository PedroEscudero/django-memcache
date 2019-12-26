FROM python:3
RUN mkdir /python
WORKDIR /python
COPY requirements.txt /python/
RUN pip install -r requirements.txt
COPY . .
