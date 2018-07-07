FROM python:3.4

# user stuff
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

# some python
COPY app/requerments.txt /requerments.txt
RUN pip install -r requerments.txt

# do some with this sht###
WORKDIR /app
COPY app /app
COPY cmd.sh /

EXPOSE 9090 9191
USER uwsgi

CMD ["/cmd.sh"]