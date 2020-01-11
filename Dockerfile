FROM python:alpine3.10
LABEL maintainer="arturo.silva@ciencias.unam.mx"

WORKDIR /usr/src/app
COPY ["app.py", "requirement.txt", "/usr/src/app/"] # Copy only *py and *.txt
RUN pip install --no-cache-dir -r requirement.txt

ENTRYPOINT python app.py
