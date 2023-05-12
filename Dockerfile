FROM python:3.9-slim-buster


WORKDIR /app

COPY requirements.txt requirements.txt

# copy source code
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

COPY requirements.txt .

# expose port
EXPOSE 80

# start the application
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
