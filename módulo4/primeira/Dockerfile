FROM python:3.11-alpine3.17

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV REDIS_HOST redis
ENV REDIS_PORT 6379

EXPOSE 8080
CMD ["python", "app.py"]
