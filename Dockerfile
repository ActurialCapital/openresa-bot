FROM python:3.9-alpine

COPY run.py /run/
COPY bot/openresa.py /bot/
COPY bot/config.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /
CMD ["python3", "run.py"]