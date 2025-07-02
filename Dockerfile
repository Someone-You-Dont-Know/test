FROM python:3.12-slim

COPY main.py .

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8000

CMD ["python", "main.py"]
