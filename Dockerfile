FROM python:3.10
EXPOSE 5000
ARG DEFAULT_USER=default_version
RUN useradd -ms /bin/bash $DEFAULT_USER
USER $DEFAULT_USER
WORKDIR /home/$DEFAULT_USER
RUN mkdir flaskapp
WORKDIR /home/$DEFAULT_USER/flaskapp
COPY /src .
RUN pip install -r requirements.txt
ENTRYPOINT [ "bash", "-x", "start_up.sh" ]