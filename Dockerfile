FROM python:3.11

RUN mkdir /catalog_of_articles_fastapi

WORKDIR /catalog_of_articles_fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /catalog_of_articles_fastapi/docker/app.sh

WORKDIR src

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
