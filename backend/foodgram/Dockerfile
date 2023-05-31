FROM python:3.7-slim

WORKDIR /app_back

COPY . .

RUN pip install -r /app_back/requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]