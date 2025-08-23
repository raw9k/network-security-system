FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r requirement.txt

EXPOSE 8000

# Run FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
