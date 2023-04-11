FROM python:3.8.16-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /workspace
WORKDIR /workspace

CMD [ "uvicorn", "main:app" ]
