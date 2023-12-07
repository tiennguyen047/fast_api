FROM python:3.10
EXPOSE 5000
RUN useradd -ms /bin/bash flask
USER flask
WORKDIR /home/flask
RUN mkdir flaskapp
WORKDIR /home/flask/flaskapp
COPY /src .
RUN pip install -r requirements.txt
ENTRYPOINT [ "bash", "-x", "start_up.sh" ]