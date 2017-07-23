FROM python:3.6.2

WORKDIR /simple-interpreter

ADD . /simple-interpreter

RUN make setup

CMD ["make", "run-repl"]
