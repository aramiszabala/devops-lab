FROM python:3.12-slim
LABEL org.opencontainers.image.source=https://github.com/aramiszabala/devops-lab

RUN useradd --create-home --uid 1000 appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

USER appuser

EXPOSE 8000

CMD ["python", "app.py"]