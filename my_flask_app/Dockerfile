FROM python:latest
LABEL authors="toxidxd"

RUN apt-get update && apt-get upgrade -y && apt-get clean -y

RUN mkdir /app

COPY requirements.txt /app/

RUN python3 -m pip install -r app/requirements.txt

COPY app.py /app

WORKDIR /app

ENTRYPOINT ["python3"]

CMD ["app.py"]
