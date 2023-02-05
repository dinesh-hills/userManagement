FROM python:3.10.9-alpine3.17

WORKDIR /app

RUN apk update
RUN apk add make mupdf-dev freetype-dev gcc g++ python3-dev

RUN pip3 install --upgrade pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "./runserver.sh" ]