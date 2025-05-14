FROM python:3.10-slim
WORKDIR /app
COPY app /app
RUN pip install flask
EXPOSE 7010
CMD ["python", "main.py"]
