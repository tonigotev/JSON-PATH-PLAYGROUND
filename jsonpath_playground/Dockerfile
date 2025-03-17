FROM python:3.9-slim

# Prevent Python from writing pyc files to disc and enable stdout/stderr logging.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "jsonpath_playground.wsgi:application", "--bind", "0.0.0.0:8000"]
