FROM python:3.10

COPY . /tableqa

WORKDIR /tableqa

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "./TableQA.py"]