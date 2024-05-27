FROM python:3.7.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
