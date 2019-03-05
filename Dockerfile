FROM python:3.7-alpine
MAINTAINER Jonatas Oliveira

ENV PYTHONUNBUFFERED 1

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install pipenv && \
    pipenv install --system

RUN apk del .tmp-build-deps

ADD ./start-app.sh /entrypoint.gunicorn.sh
RUN chmod +x /entrypoint.gunicorn.sh

ADD https://github.com/krallin/tini/releases/download/v0.10.0/tini /tini
RUN chmod +x /tini

RUN mkdir /src
WORKDIR /src
COPY . /src

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN mkdir -p /src/logs

RUN adduser -D user

RUN chown -R user:user /vol/
RUN chmod -R 775 /vol/web

RUN chown -R user:user /src && \
    chmod -R 775 /src/ && \
    chown -R user:user /src/logs && \
    chmod -R 775 /src/logs && \
    chown -R user:user /tini && \
    chmod -R 775 /tini && \
    chown -R user:user /entrypoint.gunicorn.sh && \
    chmod -R 775 /entrypoint.gunicorn.sh && \
    chown -R user:user /src/start-app.sh && \
    chmod -R 775 /src/start-app.sh

USER user

EXPOSE 5000

# ENTRYPOINT ["/tini", "--", "start-app.sh"]
