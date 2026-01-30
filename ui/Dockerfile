FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir gradio requests

EXPOSE 7860

CMD ["python", "app.py"]
