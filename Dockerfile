FROM python:3.8-slim

WORKDIR /tests

ADD . .

RUN pip install -r requirements.txt

CMD ["bash", "run_tests.sh"]