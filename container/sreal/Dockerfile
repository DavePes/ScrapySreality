FROM python:3-alpine
#WORKDIR /usr/src/app
COPY . .
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt
EXPOSE 8080
CMD [ "python3", "go_spider.py" ]
