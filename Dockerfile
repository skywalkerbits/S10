FROM alpine:3.17

WORKDIR /app

RUN apk update \
  && apk add --no-cache python3 py3-pip

COPY ./requirements.txt ./manage.py ./manage.sh ./run.py /app/
COPY ./app /app/app/

RUN pip3 install --no-cache-dir -r requirements.txt

RUN adduser --uid 1000 --disabled-password --system app

USER app

ENV DATABASE_URI sqlite://

CMD ["python3", "run.py"]
