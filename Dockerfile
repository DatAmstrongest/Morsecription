FROM python:3.12

WORKDIR /app

ENV HOST_URL=http://localhost

RUN apt-get update && apt-get install -y ffmpeg && apt-get clean

COPY main.py morse.py requirements.txt .
COPY static ./static
COPY templates templates/
COPY sounds sounds/
COPY static static/

RUN pip install -r requirements.txt

EXPOSE 5002

CMD ["python", "./main.py"]
