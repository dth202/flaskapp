# python:alpine is 3.{latest}
FROM python:alpine

LABEL source="jcdemo/flaskapp"
LABEL maintainer="Dallas Harris"

RUN pip install flask

COPY src /src/

EXPOSE 5000

VOLUME ["/src"]

ENTRYPOINT ["python", "/src/app.py"]