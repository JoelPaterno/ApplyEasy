FROM python:alpine3.12

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "--server.port=8501", "--server.address=0.0.0.0"]