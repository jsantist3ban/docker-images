FROM python:3.13.0

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
