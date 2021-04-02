FROM python:slim

LABEL org.opencontainers.image.source https://github.com/Accendit/zuyder

ADD app.py /opt/app/

ADD Pipfile* /opt/app/

WORKDIR /opt/app

RUN pip install pipenv waitress && \
    pipenv install --system

ENTRYPOINT [ "waitress-serve", "--port=80", "app:app"  ]