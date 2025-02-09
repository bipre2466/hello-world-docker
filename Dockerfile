FROM python:3.11-alpine
COPY app.py /app.py
CMD ["python", "/app.py"]