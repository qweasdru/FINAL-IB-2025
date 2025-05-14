FROM python:3.11-slim

WORKDIR /app
COPY bot/ /app/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7007
CMD ["python", "app.py"]