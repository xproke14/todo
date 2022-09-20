FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./default.conf /etc/nginx/conf.d/default.conf

USER root

RUN mkdir -p /vol/static && \
    chmod -R 755 /vol/static && \
    mkdir -p /vol/media && \
    chmod -R 755 /vol/media
